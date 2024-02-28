package com.example.termo;

import static com.example.termo.MainActivity.notificationId;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.Bundle;
import android.os.Vibrator;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.os.AsyncTask;
import android.widget.Toast;


public class MainActivity extends AppCompatActivity {
    public static final int notificationId = 1; // ID da notificação

    @Override
    protected void onCreate(Bundle savedInstanceState) {


        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Criar o canal de notificação
        createNotificationChannel();
        Server server = new Server(MainActivity.this);
        server.start();
        Intent intent = new Intent(MainActivity.this, ServerService.class);
        startService(intent);


        class SendPostTask extends AsyncTask<Void, Void, String> {
            @Override
            protected String doInBackground(Void... params) {
                String url = "http://192.168.0.192:5000/";
                String jsonBody = "{\"usuario\": \"124\", \"senha\": \"124ert\", \"porta\": 8000}";

                try {
                    return HttpPostRequest.sendPostRequest(url, jsonBody);
                } catch (IOException e) {
                    e.printStackTrace();
                    return "Erro ao enviar a requisição POST";
                }
            }

            @Override
            protected void onPostExecute(String result) {
                super.onPostExecute(result);
                Toast.makeText(MainActivity.this, result, Toast.LENGTH_SHORT).show();
            }
        }

        new SendPostTask().execute();

        Button camera = findViewById(R.id.camera);
        camera.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, SecondActivity.class);
                startActivity(intent);
            }
        });

        Button login = findViewById(R.id.logs);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, SecondActivity.class);
                startActivity(intent);
            }
        });

        Button luz = findViewById(R.id.luz);
        luz.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, SecondActivity.class);
                startActivity(intent);
            }
        });

        Button som = findViewById(R.id.som);
        som.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                vibrateDevice(500);
            }

            private void vibrateDevice(long milliseconds) {
                Vibrator vibrator = (Vibrator) getSystemService(Context.VIBRATOR_SERVICE);
                if (vibrator != null && vibrator.hasVibrator()) {
                    vibrator.vibrate(milliseconds);
                }
            }
        });
    }


    private void createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            String channelId = "ChannelID";
            String channelName = "Baba";
            String channelDescription = "Notificador";
            int importance = NotificationManager.IMPORTANCE_HIGH; // Defina a importância como alta

            NotificationChannel channel = new NotificationChannel(channelId, channelName, importance);
            channel.setDescription(channelDescription);

            NotificationManager notificationManager = getSystemService(NotificationManager.class);
            notificationManager.createNotificationChannel(channel);
        }
    }

}





