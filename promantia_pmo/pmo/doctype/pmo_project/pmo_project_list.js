// Copyright (c) 2023, Promantia Business Solutions and contributors
// For license information, please see license.txt

frappe.listview_settings["PMO_Project"] = {
	filters: [
        ["status", "=", "Active"]
    ],

    order_by: "updated_on desc",

};	