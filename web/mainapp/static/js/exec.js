
function execut(){
  $.get("/execut",function(data) {
      alert(data.message);
  },'json')
  .fail(function(data) {
      alert("error" );
  });

}
