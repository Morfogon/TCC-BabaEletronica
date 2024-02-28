package com.example.termo;

import androidx.appcompat.app.AppCompatActivity;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.io.IOException;

public class ThirdActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
    }

    public class MainActivity extends AppCompatActivity {

        private Button luz;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);

            luz = findViewById(R.id.camera);
            luz.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    // Chamada da função para enviar a requisição HTTP
                    enviarRequisicaoHttp();
                }
            });
        }

        private void enviarRequisicaoHttp() {
            // Obter a URL personalizável da requisição
            String url = "192.168.0.192:5000/iluminacao?tipo=3";

            // Configurar a requisição HTTP usando uma biblioteca como o OkHttp ou Retrofit
            OkHttpClient client = new OkHttpClient();

            // Criar um objeto Request.Builder
            Request.Builder requestBuilder = new Request.Builder()
                    .url(url);

            // Adicionar cabeçalho personalizado
            requestBuilder.addHeader("usuario", "user1");
            requestBuilder.addHeader("senha", "pass1");

            Request request = requestBuilder.build();

            new AsyncTask<Void, Void, String>() {
                @Override
                protected String doInBackground(Void... voids) {
                    try {
                        Response response = client.newCall(request).execute();
                        return response.body().string();
                    } catch (IOException e) {
                        Log.e("MainActivity", "Erro na requisição POST", e);
                    }
                    return null;
                }

                @Override
                protected void onPostExecute(String result) {
                    // Manipular a resposta da requisição aqui
                    if (result == "200") {
                        Toast.makeText(MainActivity.this, "Resposta: " + result, Toast.LENGTH_SHORT).show();
                    } else {
                        Toast.makeText(MainActivity.this, "Erro na requisição POST", Toast.LENGTH_SHORT).show();
                    }
                }
            }.execute();
        }
    }

}