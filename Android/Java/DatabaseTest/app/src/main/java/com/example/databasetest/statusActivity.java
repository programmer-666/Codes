package com.example.databasetest;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

import java.util.ArrayList;

public class statusActivity extends AppCompatActivity {
    ScrollView scrollView;
    LinearLayout linearLayout;
    ArrayList<TextView> textViews;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_status);

        scrollView = (ScrollView)findViewById(R.id.scrollView);
        linearLayout = (LinearLayout)findViewById(R.id.scrollViewLayout);

        textViews = new ArrayList<>();

        for(int i = 0;i<200;i++){
            textViews.add(new TextView(this));
            textViews.get(i).setText("deneme"+i);
            linearLayout.addView(textViews.get(i));
        }
    }
}