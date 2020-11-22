package com.example.datatransfer;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;
import androidx.viewpager.widget.ViewPager;
import androidx.viewpager2.widget.ViewPager2;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.renderscript.Element;
import android.text.Layout;
import android.text.style.TtsSpan;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.google.android.material.tabs.TabLayout;
import com.google.android.material.tabs.TabLayoutMediator;

import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Sharp extends AppCompatActivity {
    TextView txv;
    Button[] btns = new Button[5];
    TabLayout tabLayout;
    View includeitem, includeitem1, includeitem2;
//https://www.youtube.com/watch?v=meGHexSEtD0&list=PLboEI_LLbrgrrTaDCMXFVWFn_XI3YjEWQ&index=82&ab_channel=KronosApp
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sharp);
        txv = (TextView)findViewById(R.id.textView2);
        txv.setText(getIntent().getStringExtra("username"));
        btns[0] = (Button)findViewById(R.id.button2); // OUT    0
        tabLayout = (TabLayout)findViewById(R.id.tblyt);
        includeitem = (View)findViewById(R.id.includeitem0);
        includeitem1 = (View)findViewById(R.id.includeitem1);
        includeitem2 = (View)findViewById(R.id.includeitem2);
        // DEF

        // tab
        tabLayout.setOnTabSelectedListener(new TabLayout.OnTabSelectedListener() {
            @Override
            public void onTabSelected(TabLayout.Tab tab) {
                switch (tab.getPosition()){
                    case 0:
                        includeitem.setVisibility(View.VISIBLE);
                        break;
                    case 1:
                        includeitem1.setVisibility(View.VISIBLE);
                        TextView usrn = (TextView)includeitem1.findViewById(R.id.textView8);
                        TextView passw = (TextView)includeitem1.findViewById(R.id.textView9);
                        usrn.setText(txv.getText().toString());
                        passw.setText(getIntent().getStringExtra("password").toString());
                        break;
                    case 2:
                        includeitem2.setVisibility(View.VISIBLE);
                        break;
                }
            }
            @Override
            public void onTabUnselected(TabLayout.Tab tab) {
                includeitem.setVisibility(View.INVISIBLE);
                includeitem1.setVisibility(View.INVISIBLE);
                includeitem2.setVisibility(View.INVISIBLE);
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
                    case 2:
                        includeitem2.setVisibility(View.VISIBLE);
                        break;
                }
            }
        });
        // tab
        btns[0].setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent goBase = new Intent(getBaseContext(), MainActivity.class);
                startActivity(goBase);
            }
        });
    }
}
