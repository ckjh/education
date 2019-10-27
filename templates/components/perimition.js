import router from "./router";

const whiteList = ['/', '/courseDetail', '/detail','/course','/path','/BootCamp','/redisearch','/stage','/bindweibo','/member','/weibo_callback','/bindweibo','/Forgetpwd','/ShowQuestions','/Showdiscuss'];

router.beforeEach((to, from, next) => {
  var user_id = localStorage.getItem('user_id');
  if (user_id || whiteList.indexOf(to.path) != -1) {
    next()
  } else {
    next({'path': '/'})
  }
});

// const wList=[]
