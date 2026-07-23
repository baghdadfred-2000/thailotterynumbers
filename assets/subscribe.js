/* ThaiLotteryNumbers — MailerLite subscribe wiring for static (guides) pages. */
window.ml_webform_success_44063259 = function () {
  var $j = window.ml_jQuery || window.jQuery;
  if ($j) { $j('.ml-subscribe-form-44063259 .row-success').show(); $j('.ml-subscribe-form-44063259 .row-form').hide(); }
  else {
    document.querySelectorAll('.ml-subscribe-form-44063259 .row-success').forEach(function(el){el.style.display='';});
    document.querySelectorAll('.ml-subscribe-form-44063259 .row-form').forEach(function(el){el.style.display='none';});
  }
};
(function(){
  if(!document.querySelector('.ml-subscribe-form-44063259')) return;
  if(!document.getElementById('ml-webforms-js')){
    var sc=document.createElement('script'); sc.id='ml-webforms-js';
    sc.src='https://groot.mailerlite.com/js/w/webforms.min.js?v83147fa8ce2d95cb73ece7f28b469519'; sc.async=true;
    document.body.appendChild(sc);
  }
  try{ fetch('https://assets.mailerlite.com/jsonp/2528952/forms/193796763912504673/takel'); }catch(e){}
})();
