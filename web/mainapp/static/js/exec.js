
function executepy(){
  $.get("/executepy",function(data) {
      alert(data.message);
  },'json')
  .fail(function(data) {
      alert("error" );
  });

}


setTimeout(function(){
location.reload();
},3000); // 3000밀리초 = 3초


