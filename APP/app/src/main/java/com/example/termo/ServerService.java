package com.example.termo;

import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.os.IBinder;
import android.os.Vibrator;

public class ServerService extends Service {

    private Server server;
    private Context serviceContext; // Variável para armazenar o contexto do serviço

    @Override
    public void onCreate() {
        super.onCreate();
        serviceContext = this; // Armazena o contexto do serviço
        server = new Server(serviceContext);
        server.start();
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        // Você pode retornar um valor que descreve como o sistema deve
        // continuar o serviço após ele ser morto e recriado.
        return START_STICKY;
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        if (server != null) {
            server.stop(); // Certifique-se de implementar o método stop() na classe Server
        }
    }
}

