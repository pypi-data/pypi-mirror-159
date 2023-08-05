# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: unacast/v2/operator/catalog_operator_service.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
import grpclib


@dataclass(eq=False, repr=False)
class CreateCatalogRequest(betterproto.Message):
    given_id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


class CatalogOperatorServiceStub(betterproto.ServiceStub):
    """
    * This is the service used for operators to administrate the Catalogs in
    Unacat
    """

    async def create_catalog(self, *, given_id: str = "") -> "_catalog__.Catalog":

        request = CreateCatalogRequest()
        request.given_id = given_id

        return await self._unary_unary(
            "/unacast.v2.operator.CatalogOperatorService/CreateCatalog",
            request,
            _catalog__.Catalog,
        )


from .. import catalog as _catalog__
