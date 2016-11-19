
Module.register("face",{

  defaults: {
    animationSpeed: 0.5 * 1000,
  },

getDom: function() {
  var wrapper = document.createElement("div");
  switch(this.current_selection) {
    
  case "FACE";
    wrapper.innerHTML = "<img src=\"" + this.file("face.gif") + "\" style=\"border:1px solid black;max-width:100%;\">"
    break
}
})
