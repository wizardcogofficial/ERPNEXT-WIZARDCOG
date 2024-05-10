frappe.ready(function() {
	//document.body.style.backgroundColor="#1d1e22"
	var nav = document.getElementsByClassName("navbar-light")[0];
	nav.style.visibility = "hidden";
	// Select the parent div
	var parentDiv = document.querySelector('.right-area');

	// Find and remove the discard button
	var discardButton = document.querySelector('.discard-btn');
	parentDiv.removeChild(discardButton);

	// Create the anchor element to replace the discard button
	var anchorTag = document.createElement('a');
	anchorTag.href = '/home'; // Set the link URL
	anchorTag.textContent = 'Home'; // Set the text
	anchorTag.className = 'btn btn-primary btn-sm ml-2'; // Apply Bootstrap button styles
	anchorTag.style.textDecoration = 'none'; // Remove underline

	// Append the new anchor to the parent div
	parentDiv.insertBefore(anchorTag, parentDiv.children[0]); // Insert it at the position of the removed button
	 // Select the footer element
})
