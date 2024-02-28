package com.example.termo;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.webkit.WebSettings;
import java.util.HashMap;
import java.util.Map;


public class SecondActivity extends AppCompatActivity {

    private static final String TAG = "SecondActivity";
    private WebView webView;
    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        webView = findViewById(R.id.web);
        Button video = findViewById(R.id.vcamera);
        Button foto = findViewById(R.id.fcamera);

        WebSettings webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true); // Ativar JavaScript
        webView.setWebViewClient(new WebViewClient());

        // Definir uma ação ao clicar no botão
        video.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String url = "http://192.168.0.192:5000/camera?tipo=2"; // Substitua pela URL desejada

                // Cabeçalhos personalizados que você deseja passar
                Map<String, String> headers = new HashMap<>();
                headers.put("usuario", "124");
                headers.put("senha", "124ert");

                // Carregar a URL no WebView com os cabeçalhos personalizados
                webView.loadUrl(url, headers);

            }
        });
        foto.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String url = "http://192.168.0.192:5000/camera?tipo=1"; // Substitua pela URL desejada

                // Cabeçalhos personalizados que você deseja passar
                Map<String, String> headers = new HashMap<>();
                headers.put("usuario", "124");
                headers.put("senha", "124ert");

                // Carregar a URL no WebView com os cabeçalhos personalizados
                webView.loadUrl(url, headers);

            }
        });
    }
}