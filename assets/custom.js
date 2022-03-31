var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
var ev2 = new Event('input', {bubbles: true});

// document.onmousedown

document.addEventListener('mouseup', e => {

  console.log("addEventListener - mouseup - start")


  var sel = window.getSelection();
  
  var sel_str = sel.toString();
  var target_value = '';
  

  if (sel_str.length > 0) {
    var pid = e.target.id;
    if (pid == 'selection-container')
    {
      console.log("addEventListener - updating range")
      
      var range = sel.getRangeAt(0);
      target_value = `${range.startOffset}:${range.endOffset} `;

      var selection_container_element =  document.getElementById('selection-container');

      var raw_text = selection_container_element.innerText

      var forecolor = "yellow";
      var backgroundcolor = "blue";

      // <p>Here is the <mark style="color: white; background-color:red"> searched query </mark> </p>

      selection_container_element.innerHTML = 
        raw_text.slice(0, range.startOffset) + 
        "<mark style=\"color: " + forecolor  + ";" + "background-color:" + backgroundcolor + "\">" + 
        sel_str + 
        "</mark>" + raw_text.slice(range.endOffset, raw_text.length)

      // Way to set value of React input
      var text_element = document.getElementById('selection-text');
      nativeInputValueSetter.call(text_element, target_value);
      text_element.dispatchEvent(ev2);
    }
  }
  else
  {
    console.log("addEventListener - no range !!!")
  }

  console.log("addEventListener - mouseup - stop")


});

document.addEventListener('mousedown', e => {
  
  
  console.log("addEventListener - mousedown - start")
  if(e.target.id == 'selection-container')
  //if (sel.focusNode.parentNode.id == 'selection-container')
  {
    
    var selection_container_element =  document.getElementById('selection-container');

    console.log(selection_container_element)

    //document.getElementById('selection-container').innerHTML.replace(/\n|<.*?>/g,'');

    console.log("** Resetting ! ***")
    selection_container_element.innerHTML = selection_container_element.innerText;
 

    var text_element = document.getElementById('selection-text');
    nativeInputValueSetter.call(text_element, "Nothing selected");
    text_element.dispatchEvent(ev2);
  }
  console.log("addEventListener - mousedown - stop")

});