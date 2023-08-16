
document.addEventListener('DOMContentLoaded', function () {
  // Получаем все кнопки, представляющие получателей


  // Получаем все кнопки, представляющие получателей
  const recipientButtons = document.querySelectorAll('.recipient-button');

  // Переменная для хранения текущего WebSocket-соединения

  let inactivityTimer;
  const inactivityTimeout = 1000; // 10 минут в миллисекундах

  // Обработчик события клика на кнопке
  recipientButtons.forEach(button => {
    button.addEventListener('click', () => {
      const recipientUsername = button.getAttribute('data-username');

      // Устанавливаем новое WebSocket-соединение с получателем
      const chatSocket = new WebSocket('ws://localhost:8000/ws/chat/' + recipientUsername + '/');

      // Обработчик для получения сообщений через WebSocket
      chatSocket.onmessage = function (event) {
        var data = JSON.parse(event.data);
        appendMessage(data);
      };

      function appendMessage(message, isSent) {
        var messageList = document.getElementById('message-list');
        var messageDiv = document.createElement('div');
        messageDiv.textContent = message;

        if (isSent) {
          messageDiv.classList.add('sent-message');
        } else {
          messageDiv.classList.add('received-message');
        }

        messageList.appendChild(messageDiv);
      }
      function sendMessage() {
        var messageInput = document.getElementById('message-input');
        var message = messageInput.value.trim();

        if (message !== '') {
          if (chatSocket.readyState === WebSocket.OPEN) {
            chatSocket.send(JSON.stringify({
              'messagetext': message
            }));

            messageInput.value = '';
            resetInactivityTimer();

            appendMessage(message, true); // Отправленное сообщение
          } else {
            console.log('WebSocket is not open.');
          }
        }
      }

      // Обработчик для получения сообщений через WebSocket
      chatSocket.onmessage = function (event) {
        var data = JSON.parse(event.data);
        appendMessage(data.messagetext, false); // Полученное сообщение
      };

      // Функция для сброса таймера неактивности
      function resetInactivityTimer() {
        clearTimeout(inactivityTimer);
        inactivityTimer = setTimeout(closeWebSocket, inactivityTimeout);
      }

      // Функция для автоматического закрытия WebSocket-соединения
      function closeWebSocket() {
        if (chatSocket && chatSocket.readyState === WebSocket.OPEN) {
          chatSocket.close();
        }
      }

      // Обработчик для кнопки отправки сообщения
      document.getElementById('send-button').addEventListener('click', function () {
        sendMessage();
      });

      // Обработчик для поля ввода сообщения при нажатии Enter
      document.getElementById('message-input').addEventListener('keydown', function (event) {
        if (event.key === 'Enter') { // Проверяем, что нажата клавиша Enter
          sendMessage();
        }
      });

      // Обработчик для поля ввода сообщения при вводе текста
      document.getElementById('message-input').addEventListener('input', resetInactivityTimer);
    });
  });
});