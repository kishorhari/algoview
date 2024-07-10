// Copyright (c) 2024, AlogView and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client', {
    // Trigger when the form is loaded
    onload: function(frm) {
        toggle_custom_buttons(frm);
    },
    // Trigger when the controlling field is changed
    service_group: function(frm) {
        toggle_custom_buttons(frm);
    }
});

function toggle_custom_buttons(frm) {
	console.log("inside funciton")
    // Check the value of the controlling field
    if (frm.doc.service_group === 'Multi') {
        // If the condition is met, display the custom buttons
        frm.fields_dict.custom_buttons.html(`
            <div class="button-container">
                <button class="custom-button">BANKNIFTY</button>
                <button class="custom-button">NIFTY</button>
            </div>
        `);
    }else if (frm.doc.service_group === 'Cash') {
        // If the condition is met, display the custom buttons
        frm.fields_dict.custom_buttons.html(`
            <div class="button-container">
                <button class="custom-button">PPL#</button>
                <button class="custom-button">HDFCLIFE#</button>
				<button class="custom-button">HDFC#</button>
				<button class="custom-button">HDFCBANK#</button>
            </div>
        `);
    }else if (frm.doc.service_group === 'Option') {
        // If the condition is met, display the custom buttons
        frm.fields_dict.custom_buttons.html(`
            <div class="button-container">
                <button class="custom-button">BANKNIFTY</button>
                <button class="custom-button">NIFTY</button>
				<button class="custom-button">MIDCPNIFTY</button>
				<button class="custom-button">FINNIFTY</button>
            </div>
        `);
    } else {
        // If the condition is not met, hide the custom buttons
        frm.fields_dict.custom_buttons.html('');
    }

    // Add custom CSS styles
    frappe.require(['/assets/algoview/css/custom_buttons.css']);
}
