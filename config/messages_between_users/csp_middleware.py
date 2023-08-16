from django.utils.deprecation import MiddlewareMixin

class CSPMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Добавляем заголовок Content-Security-Policy для разрешения использования WebSocket
        response['Content-Security-Policy'] = "connect-src 'self' ws://localhost:8000;"

        return response




