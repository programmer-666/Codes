package com.example.musicplayerv2;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.media.MediaPlayer;
import java.util.Timer;
import java.util.TimerTask;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    ScrollView sv;
    TextView name, stt, spt;
    boolean flag = true;
    int lastMpId = 0;
    int count = 0;
    SeekBar skb;
    List<Button> buttons = new ArrayList<>();
    List<MediaPlayer> mediaPlayers = new ArrayList<>();
    String[] names = {"Hit The Lights","Jump In The Fire","Metal Militia","Motor Breath", "No Remorse", "Phantom Lord", "Pulling Teeth", "Seek And Destroy", "The Four Horseman", "Whiplash"};
    Button pb, re;

    int time;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        sv = (ScrollView)findViewById(R.id.scrl);
        LinearLayout scrly = findViewById(R.id.scrly);
        LinearLayout.LayoutParams p = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WRAP_CONTENT,
                LinearLayout.LayoutParams.FILL_PARENT);
        pb = (Button)findViewById(R.id.button2);
        re = (Button)findViewById(R.id.buttonRe);
        name = (TextView)findViewById(R.id.textView);
        stt = (TextView)findViewById(R.id.textView2);
        spt = (TextView)findViewById(R.id.textView3);
        mediaPlayers.add(MediaPlayer.create(getBaseContext(),R.raw.hitthelights));
        mediaPlayers.add(MediaPlayer.create(getBaseContext(),R.raw.jumpinthefire));
        mediaPlayers.add(MediaPlayer.create(getBaseContext(),R.raw.metalmilitia));
        mediaPlayers.add(MediaPlayer.create(getBaseContext(),R.raw.motorbreath));
        mediaPlayers.add(MediaPlayer.create(getBaseContext(),R.raw.noremorse));
        mediaPlayers.add(MediaPlayer.create(getBaseContext(),R.raw.phantomlord));
        mediaPlayers.add(MediaPlayer.create(getBaseContext(),R.raw.pullingtheeth));
        mediaPlayers.add(MediaPlayer.create(getBaseContext(),R.raw.seekanddestroy));
        mediaPlayers.add(MediaPlayer.create(getBaseContext(),R.raw.thefourhorseman));
        mediaPlayers.add(MediaPlayer.create(getBaseContext(),R.raw.whiplash));

        // # SEEKBAR STUFF
        skb.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                time = skb.getProgress()*1000;
                mediaPlayers.get(lastMpId).seekTo(time);
                return false;
            }
        });
        // # SEEKBAR STUFF

        for (int i = 0;i<10;i++){
            buttons.add(new Button(getBaseContext()));
            buttons.get(i).setText(""+names[i]);
            buttons.get(i).setBackgroundColor(Color.rgb(38,38,38));
            buttons.get(i).setTextColor(Color.rgb(255,255,255));
            scrly.addView(buttons.get(i));
        }
        // PLAYBUTTON
            pb.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    if(flag){
                        flag = false;
                        pb.setText("||");
                        mediaPlayers.get(lastMpId).start();
                        skb.setMax(mediaPlayers.get(lastMpId).getDuration()/1000);
                    }else{
                        flag = true;
                        pb.setText(">");
                        mediaPlayers.get(lastMpId).pause();
                    }
                }
            });
        // PLAYBUTTON
        // REBUTTON
        re.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mediaPlayers.get(lastMpId).seekTo(0);
            }
        });
        // REBUTTON
        // BUTTONS
            buttons.get(0).setOnClickListener(new View.OnClickListener()
            {public void onClick(View v){stuseCommand(0);}});
            buttons.get(1).setOnClickListener(new View.OnClickListener()
            {public void onClick(View v){stuseCommand(1);}});
            buttons.get(2).setOnClickListener(new View.OnClickListener()
            {public void onClick(View v){stuseCommand(2);}});
            buttons.get(3).setOnClickListener(new View.OnClickListener()
            {public void onClick(View v){stuseCommand(3);}});
            buttons.get(4).setOnClickListener(new View.OnClickListener()
            {public void onClick(View v){stuseCommand(4);}});
            buttons.get(5).setOnClickListener(new View.OnClickListener()
            {public void onClick(View v){stuseCommand(5);}});
            buttons.get(6).setOnClickListener(new View.OnClickListener()
            {public void onClick(View v){stuseCommand(6);}});
            buttons.get(7).setOnClickListener(new View.OnClickListener()
            {public void onClick(View v){stuseCommand(7);}});
            buttons.get(8).setOnClickListener(new View.OnClickListener()
            {public void onClick(View v){stuseCommand(8);}});
            buttons.get(9).setOnClickListener(new View.OnClickListener()
            {public void onClick(View v){stuseCommand(9);}});
        // BUTTONS
    }
    public void stuseCommand(int index){
        if(flag){
            flag = false;
            lastMpId = index;
            pb.setText("||");
            mediaPlayers.get(index).start();
            stt.setText(String.valueOf(mediaPlayers.get(index).getCurrentPosition()));
            name.setText(names[index]);
        }else{
            mediaPlayers.get(lastMpId).pause();
            mediaPlayers.get(lastMpId).seekTo(0);
            mediaPlayers.get(index).start();
            lastMpId = index;
            name.setText(names[index]);
            spt.setText(String.valueOf(mediaPlayers.get(index).getDuration()));
        }
    }
}