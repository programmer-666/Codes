package com.example.reinclude;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;

public class MainActivity extends AppCompatActivity {
    Button bt1 = (Button)findViewById(R.id.btn1);
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bt1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                LinearLayout dynamicContent = (LinearLayout) findViewById(R.id.dynamic_content);
                LayoutInflater layoutInflater = (LayoutInflater) this.(Context.LAYOUT_INFLATER_SERVICE);
                dynamicContent.addView(1, layoutInflater.inflate(R.layout.test_layout, this, false));
            }
        });
    }
}