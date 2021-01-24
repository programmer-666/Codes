package com.example.imageslide;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    ImageView iv;
    List<Drawable> images = new ArrayList<>();
    Button left,right;
    int count = 0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        left = (Button)findViewById(R.id.leftb);
        right = (Button)findViewById(R.id.rightb);
        iv = (ImageView)findViewById(R.id.imageView);

        images.add(getResources().getDrawable(R.drawable.chem));
        images.add(getResources().getDrawable(R.drawable.hacker));
        images.add(getResources().getDrawable(R.drawable.image));

        iv.setImageDrawable(images.get(count));
        left.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //if(images.size()>count){
                    if (count>0){
                        count-=1;
                        iv.setImageDrawable(images.get(count));
                    }else{
                        count=images.size()-1;
                        iv.setImageDrawable(images.get(count));
                    }
                //}
            }
        });
        right.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //if(count<images.size()-1){
                    if (count>images.size()){
                        count=0;
                        iv.setImageDrawable(images.get(count));
                    }else{
                        count+=1;
                        iv.setImageDrawable(images.get(count));
                    }
                //}
            }
        });
    }
}