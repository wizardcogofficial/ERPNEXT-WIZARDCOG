// window.get_product_list = function() {
// 	$(".more-btn .btn").click(function() {
// 		window.get_product_list()
// 	});

          
// 	if(window.start==undefined) {
// 		throw "product list not initialized (no start)"
// 	}

          
// 	$.ajax({
// 		method: "GET",
// 		url: "/",
// 		data: {
// 			cmd: "erpnext.templates.pages.product_search.get_product_list",
// 			start: window.start,
// 			search: window.search,
// 			product_group: window.product_group
// 		},
// 		dataType: "json",
// 		success: function(data) {
// 			window.render_product_list(data.message || []);