package com.example.musicplayercoursev;

import androidx.appcompat.app.AppCompatActivity;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.SeekBar;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    MediaPlayer mp;
    SeekBar skb;
    TextView t1,t2;
    Button playerB, m1, m2;
    int val, time;
    boolean f = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mp=MediaPlayer.create(getBaseContext(), R.raw.no_remorse);
        skb = findViewById(R.id.seekBar);
        t1 = findViewById(R.id.textView2);
        t2 = findViewById(R.id.textView3);
        playerB = findViewById(R.id.play);

        m1 = findViewById(R.id.m1);
        m2 = findViewById(R.id.m2);

        skb.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                time = skb.getProgress()*1000;
                mp.seekTo(time);
                return false;
            }
        });

        playerB.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(f){
                    f = false;
                    mp.start();
                    skb.setMax(mp.getDuration()/1000);
                    TimerSetup();
                }else{
                    f = true;
                    mp.pause();
                }
            }
        });
        m1.setOnClickListener(new View.OnClickListener() { // WHIPLASH
            @Override
            public void onClick(View v) {
                mp.stop();
                mp = MediaPlayer.create(getBaseContext(), R.raw.whiplash);
                mp.start();
                skb.setMax(mp.getDuration()/1000);
                TimerSetup();
            }
        });
        m2.setOnClickListener(new View.OnClickListener() { // NO_REMORSE
            @Override
            public void onClick(View v) {
                mp.stop();
                mp = MediaPlayer.create(getBaseContext(), R.raw.no_remorse);
                mp.start();
                skb.setMax(mp.getDuration()/1000);
                TimerSetup();
            }
        });
    }
     void TimerSetup(){
        CountDownTimer cn = new CountDownTimer(Long.MAX_VALUE, 1000) {
            @Override
            public void onTick(long millisUntilFinished) {
                val = mp.getCurrentPosition()/1000;
                t1.setText(""+val);
                t2.setText(""+mp.getDuration()/1000);
                skb.setProgress(val);
            }

            @Override
            public void onFinish() {

            }
        }.start();
    }
}