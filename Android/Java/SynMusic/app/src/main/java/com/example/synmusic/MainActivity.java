package com.example.synmusic;

import androidx.appcompat.app.AppCompatActivity;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
    Button bp;
    MediaPlayer mp;
    boolean f = true;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mp = MediaPlayer.create(getBaseContext(), R.raw.metal_militia);
        bp = (Button)findViewById(R.id.buttonPlay);
        bp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(f){
                    bp.setText("||");
                    mp.start();
                    f = false;
                }else{
                    bp.setText(">");
                    mp.pause();
                    f = true;
                }
            }
        });
    }
}