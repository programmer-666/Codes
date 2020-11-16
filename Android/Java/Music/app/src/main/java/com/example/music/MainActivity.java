package com.example.music;

import androidx.appcompat.app.AppCompatActivity;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
    MediaPlayer mp;
    Button p;
    boolean f = true;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mp = MediaPlayer.create(getBaseContext(), R.raw.laper_messiah);
        p = (Button)findViewById(R.id.buttonPlay);
        p.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(f){
                    mp.start();
                    p.setText("||");
                    f = false;
                }else{
                    mp.pause();
                    p.setText(">");
                    f = true;
                }
            }
        });
    }
}