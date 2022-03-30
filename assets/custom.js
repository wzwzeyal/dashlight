var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
var ev2 = new Event('input', {bubbles: true});

var first_time = true;
var raw_text = ''

document.addEventListener('mouseup', () => {

  var sel = window.getSelection();
  
  var sel_str = sel.toString();
  var target_value = '';
  

  if (sel_str.length > 0) {
    var pid = sel.focusNode.parentNode.id;
    if (pid == 'selection-container')
    {
      
      var range = sel.getRangeAt(0);
      target_value = `${range.startOffset}:${range.endOffset} `;

      var selection_container_element =  document.getElementById('selection-container');

      // Way to set value of React input
      var text_element = document.getElementById('selection-text');
      nativeInputValueSetter.call(text_element, target_value);
      text_element.dispatchEvent(ev2);

      var start_element = document.getElementById('selection-start');
      nativeInputValueSetter.call(start_element, range.startOffset);
      start_element.dispatchEvent(ev2);

      var end_element = document.getElementById('selection-end');
      nativeInputValueSetter.call(end_element, range.endOffset);
      end_element.dispatchEvent(ev2);

      var raw_text_element = document.getElementById('raw_text');
      nativeInputValueSetter.call(raw_text_element, selection_container_element.innerText);
      raw_text_element.dispatchEvent(ev2);     
    }
  }
});

document.addEventListener('mousedown', e => {
  
  
  if(e.target.id == 'selection-container')
  //if (sel.focusNode.parentNode.id == 'selection-container')
  {
    alert(e.target.id)
    var selection_container_element =  document.getElementById('selection-container');

    var raw_text_element = document.getElementById('raw_text2');
    nativeInputValueSetter.call(raw_text_element, selection_container_element.innerText);
    raw_text_element.dispatchEvent(ev2);   
    alert(selection_container_element.innerText)
  }

});