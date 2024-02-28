package com.example.termo;

import static com.example.termo.MainActivity.notificationId;

import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Vibrator;
import android.util.Log;

import androidx.core.app.ActivityCompat;
import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.lang.reflect.Array;
import java.net.ServerSocket;
import java.net.Socket;
import java.lang.Thread;
public class Server {

    private static final int PORT = 8000; //Porta em que vai ouvir as notificações
    //private static final String DATA = "{\"porta\":2001,\"usuario\":\"124\",\"senha\":\"124ert\"}";

    private Context context; // Contexto para notificações e vibração

    //public Server(Context context) {
    //    this.context = context;
    //}

    public Server(Context context) {
        this.context = context.getApplicationContext(); // Obter o contexto do aplicativo
    }

    public void start() {
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Inscricao();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }).start();
        //Intent intent = new Intent(context, ServerService.class);
        //context.startService(intent);
    }


    private void Inscricao() throws IOException {
        Log.d("Server", "Inscricao called");

        // Cria um servidor socket
        ServerSocket serverSocket = new ServerSocket(PORT);

        Log.d("Server", "Servidor ouvindo na porta " + PORT);

        // Loop para aceitar conexões de clientes
        while (true) {
            Socket clientSocket = serverSocket.accept();
            Log.d("Server", "Conexão recebida de " + clientSocket.getInetAddress());
            try {
                InputStream inputStream = clientSocket.getInputStream();
                OutputStream outputStream = clientSocket.getOutputStream();

                // Envia os dados para o cliente
                //outputStream.write(DATA.getBytes());

                byte[] buffer = new byte[1024];
                int bytesRead;

                // Loop para receber dados do cliente
                while ((bytesRead = inputStream.read(buffer)) != -1) {
                    String receivedData = new String(buffer, 0, bytesRead);
                    Log.d("Server", "Dados recebidos: " + receivedData);

                    // Crie e exiba a notificação
                    if (receivedData.equals("Evento de Movimentacao")){
                        showNotification("Bebe se movimentou","Notificação");
                    }
                    else if (receivedData.equals("Evento de Choro")){
                        showNotification("Bebe esta chorando","Alerta!");
                    }
                    else if (receivedData.equals("Evento de Barulho")){
                        showNotification("Som incomum detectado","Aviso");
                    }
                    else if (receivedData.equals("Evento de Risada")){
                        showNotification("Bebe esta Rindo","Notificação");
                    }
                    // Ative a vibração
                    showVibration();
                }

                outputStream.close();
                inputStream.close();
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                clientSocket.close();
            }
        }
    }

    private void showNotification(String evento, String titulo) {
        NotificationCompat.Builder builder = new NotificationCompat.Builder(context, "ChannelID")
                .setSmallIcon(R.drawable.ic_notification)
                .setContentTitle(titulo)
                .setContentText(evento)
                .setPriority(NotificationCompat.PRIORITY_HIGH)
                .setVisibility(NotificationCompat.VISIBILITY_PUBLIC);

        NotificationManagerCompat notificationManager = NotificationManagerCompat.from(context);
        if (ActivityCompat.checkSelfPermission(context, android.Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED) {
            return;
        }
        notificationManager.notify(notificationId, builder.build());
    }

    private void showVibration() {
        try {
            Vibrator vibrator = (Vibrator) context.getSystemService(Context.VIBRATOR_SERVICE);
            if (vibrator != null) {
                //vibrator.vibrate(500);
                // Não há necessidade de Thread.sleep() aqui
                //vibrator.vibrate(500);
                long[] pattern = {100, 200, 100, 200, 100, 200};
                vibrator.vibrate(pattern, -1);
            }
        } catch (Exception e) {
            Log.d("Erro", "" + e);
        }
    }


    public void stop() {
    }
}