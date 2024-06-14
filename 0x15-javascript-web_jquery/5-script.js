$(document).ready(function() {
  $("#add_item").click(function() {
    const newItem = $("<li>Item</li>");  // Create new li element
    $("ul.my_list").append(newItem);    // Append it to the list
  });
});
