// Функция для вывода разрешений из CSP
function displayCspDirectives() {
    var cspMeta = document.querySelector('meta[http-equiv="Content-Security-Policy"]');
    if (cspMeta) {
      var cspContent = cspMeta.getAttribute('content');
      var directives = cspContent.split(';');
  
      console.log('Content Security Policy Directives:');
      directives.forEach(function (directive) {
        console.log(directive.trim());
      });
    } else {
      console.log('No Content Security Policy meta tag found.');
    }
  }
  
  // Вызываем функцию для вывода разрешений
  displayCspDirectives();
  

  function checkCSP() {
    const cspDirectives = document.querySelectorAll('csp-error-output.js');
  
    cspDirectives.forEach(directive => {
      const directiveValue = directive.textContent;
      
      if (directiveValue.includes("connect-src 'self' ws:")) {
        console.log("WebSocket connection is blocked by CSP.");
        console.log("Consider adding 'ws:<URL>' to your CSP connect-src directive.");
      }
    });
  }
  
//   Вызываем функцию для проверки CSP
  checkCSP();
  