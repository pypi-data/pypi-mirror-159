from __future__ import annotations

import typing as t
from typing import TYPE_CHECKING

from starlette.requests import Request
from multipart.multipart import parse_options_header
from starlette.responses import Response

from .base import IODescriptor
from ...exceptions import InvalidArgument
from ...exceptions import BentoMLException
from ..utils.formparser import populate_multipart_requests
from ..utils.formparser import concat_to_multipart_response

if TYPE_CHECKING:
    from types import UnionType

    from ..types import LazyType
    from ..context import InferenceApiContext as Context


class Multipart(IODescriptor[t.Any]):
    """
    :code:`Multipart` defines API specification for the inputs/outputs of a Service, where inputs/outputs
    of a Service can receive/send a *multipart* request/responses as specified in your API function signature.

    Sample implementation of a sklearn service:

    .. code-block:: python

        # sklearn_svc.py
        import bentoml
        from bentoml.io import NumpyNdarray, Multipart, JSON
        import bentoml.sklearn

        runner = bentoml.sklearn.get("sklearn_model_clf").to_runner()

        svc = bentoml.Service("iris-classifier", runners=[runner])
        input_spec = Multipart(arr=NumpyNdarray(), annotations=JSON())
        output_spec = Multipart(output=NumpyNdarray(), result=JSON())

        @svc.api(input=input_spec, output=output_spec)
        def predict(arr, annotations):
            res = runner.run(arr)
            return {"output":res, "result":annotations}

    Users then can then serve this service with :code:`bentoml serve`:

    .. code-block:: bash

        % bentoml serve ./sklearn_svc.py:svc --reload

        (Press CTRL+C to quit)
        [INFO] Starting BentoML API server in development mode with auto-reload enabled
        [INFO] Serving BentoML Service "iris-classifier" defined in "sklearn_svc.py"
        [INFO] API Server running on http://0.0.0.0:3000

    Users can then send requests to the newly started services with any client:

    .. tabs::

        .. code-tab:: python

            import requests
            from requests_toolbelt.multipart.encoder import MultipartEncoder

            m = MultipartEncoder(
                fields={'field0': 'value', 'field1': 'value',
                        'field2': ('filename', open('test.json', 'rb'), 'application/json')}
                )

            requests.post('http://0.0.0.0:3000/predict', data=m, headers={'Content-Type': m.content_type})

        .. code-tab:: bash

            % curl -X POST -H "Content-Type: multipart/form-data" -F annotations=@test.json -F arr='[5,4,3,2]' http://0.0.0.0:3000/predict

            --b1d72c201a064ecd92a17a412eb9208e
            Content-Disposition: form-data; name="output"
            content-length: 1
            content-type: application/json

            1
            --b1d72c201a064ecd92a17a412eb9208e
            Content-Disposition: form-data; name="result"
            content-length: 13
            content-type: application/json

            {"foo":"bar"}
            --b1d72c201a064ecd92a17a412eb9208e--

    Args:
        inputs (:code:`Dict[str, IODescriptor]`):
            Dictionary consisting keys as inputs definition for a Multipart
            request/response, values as IODescriptor supported by BentoML. Currently,
            Multipart supports Image, NumpyNdarray, PandasDataFrame, PandasSeries, Text,
            and File.

            Make sure to match the input params in an API function to the keys defined
            under :code:`Multipart`:

            .. code-block:: bash

                +----------------------------------------------------------------+
                |                                                                |
                |   +--------------------------------------------------------+   |
                |   |                                                        |   |
                |   |    Multipart(arr=NumpyNdarray(), annotations=JSON())   |   |
                |   |                                                        |   |
                |   +----------------+-----------------------+---------------+   |
                |                    |                       |                   |
                |                    |                       |                   |
                |                    |                       |                   |
                |                    +----+        +---------+                   |
                |                         |        |                             |
                |         +---------------v--------v---------+                   |
                |         |  def predict(arr, annotations):  |                   |
                |         +----------------------------------+                   |
                |                                                                |
                +----------------------------------------------------------------+

    Returns:
        :obj:`~bentoml._internal.io_descriptors.IODescriptor`: IO Descriptor that Multipart request/response.
    """

    def __init__(self, **inputs: IODescriptor[t.Any]):
        for descriptor in inputs.values():
            if isinstance(descriptor, Multipart):  # pragma: no cover
                raise InvalidArgument(
                    "Multipart IO can not contain nested Multipart IO descriptor"
                )
        self._inputs: dict[str, t.Any] = inputs

    def input_type(
        self,
    ) -> dict[str, t.Type[t.Any] | UnionType | LazyType[t.Any]]:
        res: dict[str, t.Type[t.Any] | UnionType | LazyType[t.Any]] = {}
        for (k, v) in self._inputs.items():
            inp_type = v.input_type()
            if isinstance(inp_type, dict):
                raise TypeError(
                    "A multipart descriptor cannot take a multi-valued I/O descriptor as input"
                )
            res[k] = inp_type

        return res

    def openapi_schema_type(self) -> dict[str, t.Any]:
        return {
            "type": "object",
            "properties": {
                k: io.openapi_schema_type() for (k, io) in self._inputs.items()
            },
        }

    def openapi_request_schema(self) -> dict[str, t.Any]:
        """Returns OpenAPI schema for incoming requests"""
        return {"multipart/form-data": {"schema": self.openapi_schema_type()}}

    def openapi_responses_schema(self) -> dict[str, t.Any]:
        """Returns OpenAPI schema for outcoming responses"""
        return {"multipart/form-data": {"schema": self.openapi_schema_type()}}

    async def from_http_request(self, request: Request) -> dict[str, t.Any]:
        ctype, _ = parse_options_header(request.headers["content-type"])
        if ctype != b"multipart/form-data":
            raise BentoMLException(
                f"{self.__class__.__name__} only accepts `multipart/form-data` as Content-Type header, got {ctype} instead."
            )

        res: dict[str, t.Any] = dict()
        reqs = await populate_multipart_requests(request)

        for k, i in self._inputs.items():
            req = reqs[k]
            v = await i.from_http_request(req)
            res[k] = v
        return res

    async def to_http_response(
        self, obj: dict[str, t.Any], ctx: Context | None = None
    ) -> Response:
        res_mapping: dict[str, Response] = {}
        for k, io_ in self._inputs.items():
            data = obj[k]
            resp = io_.init_http_response()
            res_mapping[k] = await io_.finalize_http_response(resp, data)
        return await concat_to_multipart_response(res_mapping, ctx)
