// Copyright (c) 2016, Ebkar Technology. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Technician Commission"] = {
	"filters": [
		{
			fieldname: "technician",
			label: "Technician",
			fieldtype: "Link",
			reqd: 1,
			options: "Employee",
			get_query: function () {
				return {
					"filters": {
						"technician_gets_a_commission": 1
					}
				}
			}
		},
		{
			fieldname:"from_date",
			reqd: 1,
			label: __("From Date"),
			fieldtype: "Date",
			default: frappe.datetime.add_months(frappe.datetime.get_today(), -1),
		},
		{
			fieldname:"to_date",
			reqd: 1,
			default: frappe.datetime.get_today(),
			label: __("To Date"),
			fieldtype: "Date",
		},
		{
			fieldname:"sales_invoice",
			label: __("Sales Invoice"),
			fieldtype: "Link",
			options: "Sales Invoice"
		},
		{
			fieldname:"item",
			label: __("Item"),
			fieldtype: "Link",
			options: "Item"
		},
		{
			fieldname:"item_group",
			label: __("Item Group"),
			fieldtype: "Link",
			options: "Item Group"
		},
		{
			fieldname:"currency",
			default: frappe.defaults.get_default("currency"),
			label: __("Currency"),
			fieldtype: "Link",
			options: "Currency"
		},
	]
};
