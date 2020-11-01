// progressbar.js@1.0.0 version is used
// Docs: http://progressbarjs.readthedocs.org/en/1.0.0/
document.addEventListener('DOMContentLoaded', function(){ 
  function DrawProgressCircle(idcont) {
      let el=document.getElementById(idcont);
      var bar = new ProgressBar.Circle("#"+idcont, {
      color: '#B5E742',
      // This has to be the same size as the maximum width to
      // prevent clipping
      strokeWidth: 4,
      trailWidth: 1,
      easing: 'easeInOut',
      duration: 1400,
      text: {
        autoStyleContainer: false
      },
      from: { color: '#B5E742', width: 1 },
      to: { color: '#B5E742', width: 4 },
      // Set default step function for all animate calls
      step: function(state, circle) {
        circle.path.setAttribute('stroke', state.color);
        circle.path.setAttribute('stroke-width', state.width);

        var value = Math.round(circle.value() * el.dataset.valuemax);
        if (value === 0) {
          circle.setText('');
        } else {
            let proc_value = value % 10
            let ball = ''
            if (value == 0) {
                ball = 'баллов'
            }
            else if (proc_value == 0 || proc_value >= 5) {
                ball = 'баллов'
            }
            else if (value >= 11 && value <= 19) {
                ball = 'баллов'
            }
            else if (proc_value == 1) {
                ball = 'балл'
            }
            else {
                ball = 'балла'
            }
          circle.setText(value + '<br>' + ball);
        }

      }

  });
  bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
  bar.text.style.fontSize = '2rem';

  bar.animate(el.dataset.count/el.dataset.valuemax);  // Number from 0.0 to 1.0
}

  DrawProgressCircle("container1");
  DrawProgressCircle("container2");
  DrawProgressCircle("container3");
  DrawProgressCircle("container4");
  DrawProgressCircle("container5");
  DrawProgressCircle("container6");
});



 