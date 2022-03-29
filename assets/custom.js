document.addEventListener('mouseup', () => {
  var sel = window.getSelection();
  var sel_str = sel.toString();
  var target_value = '';
  var range = sel.getRangeAt(0);

  if (sel_str.length > 0) {
    var pid = sel.focusNode.parentNode.id;
    if (pid == 'selection-container') {
      // target_value = sel_str;
      
      
      // var newNode = document.createElement("mark");
      // range.surroundContents(newNode);
      
      target_value =  `Selected text is in the range ${range.startOffset}:${range.endOffset} `;
      // target_value = 
    }
  }
  
  // Way to set value of React input
  var text_element = document.getElementById('selection-text');
  var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
  nativeInputValueSetter.call(text_element, target_value);
  var ev2 = new Event('input', {bubbles: true});
  text_element.dispatchEvent(ev2);

  var start_element = document.getElementById('selection-start');
  var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
  nativeInputValueSetter.call(start_element, range.startOffset);
  var ev2 = new Event('input', {bubbles: true});
  start_element.dispatchEvent(ev2);

  var end_element = document.getElementById('selection-end');
  var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
  nativeInputValueSetter.call(end_element, range.endOffset);
  var ev2 = new Event('input', {bubbles: true});
  end_element.dispatchEvent(ev2);

});