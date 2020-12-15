package com.example.killemall;

import androidx.appcompat.app.AppCompatActivity;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.SeekBar;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    MediaPlayer mp;
    SeekBar skb;
    TextView starttext, stoptext;
    Button playerB, hit, four, motor, jump;
    boolean status = false;
    int val, time;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        starttext = findViewById(R.id.startDateText);
        stoptext = findViewById(R.id.stopTextDate);

        skb = findViewById(R.id.seekBar);

        mp = MediaPlayer.create(getBaseContext(), R.raw.hitthelights);

        playerB = findViewById(R.id.playPauseButton);
        hit = findViewById(R.id.hitthB);
        four = findViewById(R.id.fourB);
        motor = findViewById(R.id.motorB);
        jump = findViewById(R.id.jumpB);
        // SEEKBAR TOUCH
        skb.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                time = skb.getProgress()*1000;
                mp.seekTo(time);
                return false;
            }
        });
        // SEEKBAR TOUCH
        // PLAY BUTTON
        playerB.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(status){
                    playerStart();
                }else{
                    playerStop();
                }
            }
        });
        // PLAY BUTTON
        // MUSIC BUTTONS
        hit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                changeMusic(R.raw.hitthelights);
            }
        });
        four.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                changeMusic(R.raw.thefourhorseman);
            }
        });
        motor.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                changeMusic(R.raw.motorbreath);
            }
        });
        jump.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                changeMusic(R.raw.jumpinthefire);
            }
        });
        // MUSIC BUTTONS
    }
    void changeMusic(int rid){
        playerStop();
        mp = MediaPlayer.create(getBaseContext(), rid);
        playerStart();
        skb.setMax(mp.getDuration()/1000);
        backTimerSetup();
    }
    void backTimerSetup(){
        CountDownTimer cnt = new CountDownTimer(Long.MAX_VALUE, 1000) {
            @Override
            public void onTick(long millisUntilFinished) {
                val = mp.getCurrentPosition()/1000;
                microToMinute(mp.getCurrentPosition()/1000, starttext);
                microToMinute(mp.getDuration()/1000, stoptext);
                skb.setProgress(val);
            }
            @Override
            public void onFinish(){}
        }.start();
    }
    void playerStart(){
        playerB.setText("||");
        status = false;
        mp.start();
    }
    void playerStop(){
        playerB.setText(">");
        status = true;
        mp.pause();
    }
    void microToMinute(int mcs, TextView rid){
        float min = (float)(mcs-(mcs%60))/60;
        float sec = (float)mcs%60;
        if(sec<10){
            rid.setText(""+(int)min+":0"+(int)sec);
        }else{
            rid.setText(""+(int)min+":"+(int)sec);
        }
    }
}