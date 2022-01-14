#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @version    2021.39
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from src.models.lockstep_response import LockstepResponse
from src.models.invoicemodel import InvoiceModel

class InvoicesClient:
    from src.lockstep_api.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    """
    Retrieves the Invoice specified by this unique identifier, 
    optionally including nested data sets. 

    An Invoice represents a bill sent from one company to another. The 
    creator of the invoice is identified by the `CompanyId` field, and 
    the recipient of the invoice is identified by the `CustomerId` 
    field. Most invoices are uniquely identified both by a Lockstep 
    Platform ID number and a customer ERP "key" that was generated by 
    the system that originated the invoice. Invoices have a total amount 
    and a due date, and when some payments have been made on the Invoice 
    the `TotalAmount` and the `OutstandingBalanceAmount` may be 
    different.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of this invoice; NOT the 
        customer's ERP key
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: Addresses, Lines, 
        Payments, Notes, Attachments, Company, Customer, CustomFields, 
        CreditMemos
    """
    def retrieve_invoice(self, id: str, include: str) -> LockstepResponse:
        path = f"/api/v1/Invoices/{id}"
        return self.client.send_request("GET", path, None, {id: str, include: str})

    """
    Updates an existing Invoice with the information supplied to this 
    PATCH call. 

    The PATCH method allows you to change specific values on the object 
    while leaving other values alone. As input you should supply a list 
    of field names and new values. If you do not provide the name of a 
    field, that field will remain unchanged. This allows you to ensure 
    that you are only updating the specific fields desired. An Invoice 
    represents a bill sent from one company to another. The creator of 
    the invoice is identified by the `CompanyId` field, and the 
    recipient of the invoice is identified by the `CustomerId` field. 
    Most invoices are uniquely identified both by a Lockstep Platform ID 
    number and a customer ERP "key" that was generated by the system 
    that originated the invoice. Invoices have a total amount and a due 
    date, and when some payments have been made on the Invoice the 
    `TotalAmount` and the `OutstandingBalanceAmount` may be different.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of the invoice to update; 
        NOT the customer's ERP key
    body : object
        A list of changes to apply to this Invoice
    """
    def update_invoice(self, id: str, body: object) -> LockstepResponse:
        path = f"/api/v1/Invoices/{id}"
        return self.client.send_request("PATCH", path, body, {id: str, body: object})

    """
    Deletes the Invoice referred to by this unique identifier. An 
    Invoice represents a bill sent from one company to another. The 
    creator of the invoice is identified by the `CompanyId` field, and 
    the recipient of the invoice is identified by the `CustomerId` 
    field. Most invoices are uniquely identified both by a Lockstep 
    Platform ID number and a customer ERP "key" that was generated by 
    the system that originated the invoice. Invoices have a total amount 
    and a due date, and when some payments have been made on the Invoice 
    the `TotalAmount` and the `OutstandingBalanceAmount` may be 
    different.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of the invoice to delete; 
        NOT the customer's ERP key
    """
    def delete_invoice(self, id: str) -> LockstepResponse:
        path = f"/api/v1/Invoices/{id}"
        return self.client.send_request("DELETE", path, None, {id: str})

    """
    Creates one or more Invoices within this account and returns the 
    records as created. 

    An Invoice represents a bill sent from one company to another. The 
    creator of the invoice is identified by the `CompanyId` field, and 
    the recipient of the invoice is identified by the `CustomerId` 
    field. Most invoices are uniquely identified both by a Lockstep 
    Platform ID number and a customer ERP "key" that was generated by 
    the system that originated the invoice. Invoices have a total amount 
    and a due date, and when some payments have been made on the Invoice 
    the `TotalAmount` and the `OutstandingBalanceAmount` may be 
    different.

    Parameters
    ----------
    body : list[InvoiceModel]
        The Invoices to create
    """
    def create_invoices(self, body: list[InvoiceModel]) -> LockstepResponse:
        path = f"/api/v1/Invoices"
        return self.client.send_request("POST", path, body, {body: list[InvoiceModel]})

    """
    Queries Invoices for this account using the specified filtering, 
    sorting, nested fetch, and pagination rules requested. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. An Invoice represents a bill 
    sent from one company to another. The creator of the invoice is 
    identified by the `CompanyId` field, and the recipient of the 
    invoice is identified by the `CustomerId` field. Most invoices are 
    uniquely identified both by a Lockstep Platform ID number and a 
    customer ERP "key" that was generated by the system that originated 
    the invoice. Invoices have a total amount and a due date, and when 
    some payments have been made on the Invoice the `TotalAmount` and 
    the `OutstandingBalanceAmount` may be different.

    Parameters
    ----------
    filter : str
        The filter for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: Addresses, Lines, 
        Payments, Notes, Attachments, Company, Customer, CustomFields, 
        CreditMemos
    order : str
        The sort order for this query. See See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageSize : int
        The page size for results (default 200). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageNumber : int
        The page number for results (default 0). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    """
    def query_invoices(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/Invoices/query"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})

    """
    Queries Invoices for this account using the specified filtering, 
    sorting, nested fetch, and pagination rules requested. Display the 
    results using the Invoice Summary View format. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. 

    The Invoice Summary View represents a slightly different view of the 
    data and includes some extra fields that might be useful. For more 
    information, see the data format of the Invoice Summary Model.

    Parameters
    ----------
    filter : str
        The filter for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. No collections are currently available but 
        may be offered in the future
    order : str
        The sort order for this query. See See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageSize : int
        The page size for results (default 200). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageNumber : int
        The page number for results (default 0). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    """
    def query_invoice_summary_view(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/Invoices/views/summary"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})

    """
    Queries At Risk Invoices for this account using the specified 
    filtering, sorting, nested fetch, and pagination rules requested. 
    Display the results using the At Risk Invoice Summary View format. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. 

    The At Risk Invoice Summary View represents a slightly different 
    view of the data and includes some extra fields that might be 
    useful. For more information, see the data format of the At Risk 
    Invoice Summary Model.

    Parameters
    ----------
    filter : str
        The filter for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. No collections are currently available but 
        may be offered in the future
    order : str
        The sort order for this query. See See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageSize : int
        The page size for results (default 200). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageNumber : int
        The page number for results (default 0). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    """
    def query_at_risk_invoice_summary_view(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/Invoices/views/at-risk-summary"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})
