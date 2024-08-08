
frappe.ui.form.on('Option Chain', {
    symbol: function(frm) {
        frm.add_custom_button(__('Fetch NSE Data'), function() {
           
			frappe.call({
				method: 'algoview.algoview.option_chain.fetch_and_post_nse_data',
				args: {
					symbol: cur_frm.doc.symbol
				},
				callback: function(r) {
					if(r.message) {
						frappe.msgprint(__('NSE data fetched and posted successfully'));
					}
				}
			});
        });
    }
});
