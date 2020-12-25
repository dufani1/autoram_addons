# Copyright (c) 2013, Ebkar Technology. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _
import frappe

def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)


	return columns, data

def get_columns(filters):
	return [
		{
			"fieldname": "technician_name",
			"label": _("Technician Name"),
			"fieldtype": "Link",
			"options": "Employee",
			"width": "176"
		},
		{
			"fieldname": "invoice_name",
			"label": _("Invoice"),
			"fieldtype": "Link",
			"options": "Sales Invoice",
			"width": "144"
		},
		{
			"fieldname": "invoice_currency",
			"label": _("Currency"),
			"fieldtype": "Link",
			"options": "Currency",
			"width": "64"
		},
		{
			"fieldname": "item_name",
			"label": _("Item"),
			"fieldtype": "Link",
			"options": "Item",
			"width": "180"
		},
		{
			"fieldname": "item_uom",
			"label": _("UOM"),
			"fieldtype": "Link",
			"options": "UOM",
			"width": "50"
		},
				{
			"fieldname": "item_qty",
			"label": _("Quantity"),
			"fieldtype": "Data",
			"width": "73"
		},
		{
			"fieldname": "amount",
			"label": _("Amount"),
			"fieldtype": "Currency",
			"width": "150"
		},
		{
			"fieldname": "commission",
			"label": _("Commission Amount"),
			"fieldtype": "Currency",
			"width": "135"
		},
		{
			"fieldname": "commission_rate",
			"label": _("Commission Rate"),
			"fieldtype": "Currency",
			"width": "120"
		}
	]

def get_data(filters):
	tmp_row = {}
	idx = 0
	filters_dict = {}
	data = []
	si_orm = None

	if(filters.get("from_date")):
		filters_dict["posting_date"] = [">=", filters.get("from_date"), "<=", filters.get("to_date")]

	if(filters.get("currency")):
		filters_dict["currency"] = filters.get("currency")

	si_list = frappe.get_all("Sales Invoice", fields=["name", "currency"], filters=filters_dict)
	
	while(idx < len(si_list)):
		# get si orm for each si list item
		si_orm = frappe.get_doc("Sales Invoice", si_list[idx].name)

		for item in si_orm.items:
			if item.technician != filters.technician:
				continue
			tmp_row = {
				"technician_name": item.technician_name,
				"invoice_name": si_orm.name,
				"invoice_currency": si_list[idx].currency,
				"item_name": item.item_name,
				"item_uom": item.uom,
				"item_qty": frappe.utils.flt(item.qty),
				"amount": item.amount,
				"commission": frappe.format_value(item.technician_commission_amount, "Currency"),
				"commission_rate": frappe.format_value(item.technician_commission_rate, "Currency")
			}
			data.append(tmp_row)
			
		idx+=1

	return data