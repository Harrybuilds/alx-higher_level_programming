$(document).ready(function() {
  $("#toggle_header").click(function() {
    const header = $("header");
    const currentClass = header.attr("class");

    // Determine new class based on current class
    let newClass;
    if (currentClass.includes("red")) {
      newClass = "green";
    } else {
      newClass = "red";
    }

    // Remove existing class and add the new class
    header.removeClass(currentClass).addClass(newClass);
  });
});
