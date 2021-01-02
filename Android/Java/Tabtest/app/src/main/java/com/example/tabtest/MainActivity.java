package com.example.tabtest;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.material.tabs.TabLayout;

public class MainActivity extends AppCompatActivity {
    TextView txv;
    TabLayout tabLayout;
    View includeitem, includeitem1, includeitem2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tabLayout = (TabLayout)findViewById(R.id.tblyt);
        includeitem = (View)findViewById(R.id.includeitem0);
        includeitem1 = (View)findViewById(R.id.includeitem2);


        tabLayout.setOnTabSelectedListener(new TabLayout.OnTabSelectedListener() {
            @Override
            public void onTabSelected(TabLayout.Tab tab) {
                switch (tab.getPosition()){
                    case 0:
                        includeitem.setVisibility(View.VISIBLE);
                        Toast.makeText(MainActivity.this, "0 selected", Toast.LENGTH_SHORT).show();
                        break;
                    case 1:
                        includeitem1.setVisibility(View.VISIBLE);
                        Toast.makeText(MainActivity.this, "1 selected", Toast.LENGTH_SHORT).show();
                        break;
                }
            }

            @Override
            public void onTabUnselected(TabLayout.Tab tab) {
                includeitem.setVisibility(View.INVISIBLE);
                includeitem1.setVisibility(View.INVISIBLE);
            }

            @Override
            public void onTabReselected(TabLayout.Tab tab) {
                switch (tab.getPosition()){
                    case 0:
                        includeitem.setVisibility(View.VISIBLE);
                        break;
                    case 1:
                        includeitem1.setVisibility(View.VISIBLE);
                        break;
                }
            }
        });
    }
}