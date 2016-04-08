package com.opencv.andy.vision;

import com.opencv.andy.vision.authenticator.BootstrapAuthenticatorActivity;
import com.opencv.andy.vision.core.TimerService;
import com.opencv.andy.vision.ui.BootstrapActivity;
import com.opencv.andy.vision.ui.BootstrapFragmentActivity;
import com.opencv.andy.vision.ui.BootstrapTimerActivity;
import com.opencv.andy.vision.ui.CheckInsListFragment;
import com.opencv.andy.vision.ui.MainActivity;
import com.opencv.andy.vision.ui.NavigationDrawerFragment;
import com.opencv.andy.vision.ui.NewsActivity;
import com.opencv.andy.vision.ui.NewsListFragment;
import com.opencv.andy.vision.ui.UserActivity;
import com.opencv.andy.vision.ui.UserListFragment;

import javax.inject.Singleton;

import dagger.Component;

@Singleton
@Component(
        modules = {
                AndroidModule.class,
                BootstrapModule.class
        }
)
public interface BootstrapComponent {

    void inject(BootstrapApplication target);

    void inject(BootstrapAuthenticatorActivity target);

    void inject(BootstrapTimerActivity target);

    void inject(MainActivity target);

    void inject(CheckInsListFragment target);

    void inject(NavigationDrawerFragment target);

    void inject(NewsActivity target);

    void inject(NewsListFragment target);

    void inject(UserActivity target);

    void inject(UserListFragment target);

    void inject(TimerService target);

    void inject(BootstrapFragmentActivity target);
    void inject(BootstrapActivity target);


}
