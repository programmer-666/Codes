package com.example.tablayouttest;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;
import androidx.viewpager.widget.ViewPager;

import android.os.Bundle;

import com.google.android.material.tabs.TabLayout;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    TabLayout tabLayout;
    ViewPager viewPager;
    ArrayList<String> arrayList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        tabLayout = (TabLayout)findViewById(R.id.tabLayout1);
        viewPager = (ViewPager)findViewById(R.id.viewPager1);
        arrayList = new ArrayList<>();
        arrayList.add("Wallet");
        arrayList.add("Profile");
        arrayList.add("Send");
        arrayList.add("Get");
        prepareMainFragment();
    }

    private void prepareMainFragment(ViewPager viewPager, ArrayList<String> arrayList) {
        MainAdapter a dapter = new MainAdapter(getSupportFragmentManager());
        MainFragment fragment = new MainFragment();
    }

    private class MainAdapter extends FragmentPagerAdapter{
        ArrayList<String> arrayList = new ArrayList<>();
        List<Fragment> fragmentList = new ArrayList<>();
        public MainAdapter(@NonNull FragmentManager fm) {
            super(fm);
        }
        public void getFragment(Fragment fragment, String title){
            fragmentList.add(fragment);
            arrayList.add(title);
        }
        @NonNull
        @Override
        public Fragment getItem(int position) {
            return fragmentList.get(position);
        }

        @Override
        public int getCount() {
            return fragmentList.size();
        }
    }
}