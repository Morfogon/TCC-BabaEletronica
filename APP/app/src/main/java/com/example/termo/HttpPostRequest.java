package com.example.termo;
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class HttpPostRequest {

    public static String sendPostRequest(String url, String jsonData) throws IOException {
        HttpURLConnection connection = null;

        try {
            URL requestUrl = new URL(url);
            connection = (HttpURLConnection) requestUrl.openConnection();

            // Configurar a conexão para o método POST
            connection.setRequestMethod("POST");
            connection.setDoOutput(true);
            // Configurar os cabeçalhos
            connection.setRequestProperty("Content-Type", "application/json");

            // Escrever os dados JSON no corpo da requisição
            try (DataOutputStream wr = new DataOutputStream(connection.getOutputStream())) {
                wr.write(jsonData.getBytes(StandardCharsets.UTF_8));
                wr.flush();
            }

            // Ler a resposta do servidor
            StringBuilder response = new StringBuilder();
            try (BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while ((line = in.readLine()) != null) {
                    response.append(line);
                }
            }

            return response.toString();
        } finally {
            if (connection != null) {
                connection.disconnect();
            }
        }
    }
}
