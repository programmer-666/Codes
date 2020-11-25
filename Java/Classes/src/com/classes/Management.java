package com.classes;

public class Management {
    private static String[] jobs = new String[5];
    public void AddJob(String Jobname){
        jobs[0] = Jobname;
    }
    public void FinishJob(){
        jobs[0] = null;
    }
    public void ShowJobs(){
        System.out.println(jobs[0]);
    }
}
