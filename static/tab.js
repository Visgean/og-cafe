// This file controls tabs  



//defining variables
var pwd=window.location.pathname;
var pwd_main =pwd.split("/")[3]              // application name from current adress, for example /cafe/cashbox/manager/
                                             // usually we want the last part, eg /manager/

tabs = document.getElementsByTagName("li");

for (var i=0; i < tabs.length; i++) {
  var tab = tabs[i];
  
  if (tab.id == pwd_main && tab.className == "tab") 
      {
        tab.className = "active";
      }
     
}
