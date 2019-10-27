<template>
  <div>
    <header1 v-if="isRouterAlive"></header1>
    <div class="navbar-banner layout-no-margin-top">
      <div class="banner-container">
        <div class="container">
          <div class="row">
            <div class="col-md-7">
              <a class="container-title">
                <img src="/static/img/container-title-2.png"/>
              </a>
              <div style="margin-top:24px;">
                <a id="course-btn" class="course-btn btn btn-lg" href="/course">进入课程</a>
              </div>
            </div>

            <div class="col-md-5">

<!--              <form action="/quickregister" method="post">-->
<!--                <div class="form-group">-->
<!--                  <input class="form-control" name="name" id="name" type="text" placeholder="昵称">-->
<!--                  <div class="help-block text-left"></div>-->
<!--                </div>-->
<!--                <div class="form-group">-->
<!--                  <input class="form-control" name="email" id="email" type="email" placeholder="邮箱">-->
<!--                  <div class="help-block text-left"></div>-->
<!--                </div>-->
<!--                <div class="form-group">-->
<!--                  <input class="form-control" name="password" id="password" type="password" placeholder="密码">-->
<!--                  <div class="help-block text-left"></div>-->
<!--                </div>-->
<!--                <button class="btn register" type="submit">加入实验楼</button>-->
<!--                <p class="tip">点击"加入实验楼"，表示您已经同意我们的<a href="privacy/index.html" target="_blank"> 隐私条款</a></P>-->
<!--              </form>-->

            </div>

          </div>
        </div>
      </div>
    </div>

    <div class="introduce-container" id="fourFeatures">
      <div class="container">
        <div class="row">
          <div class="introduce-unit col-sm-6 col-md-3">
            <div><a class="introduce-img"><img src="/static/img/introduceContainer1.gif"/></a></div>
            <div><span class="introduce-span">丰富全面的计算机实验课程</span></div>
          </div>
          <div class="introduce-unit col-sm-6 col-md-3">
            <div><a class="introduce-img"><img src="/static/img/introduceContainer2.gif"/></a></div>
            <div><span class="introduce-span">在线编程环境，1秒启动</span></div>
          </div>
          <div class="introduce-unit col-sm-6 col-md-3">
            <div><a class="introduce-img"><img src="/static/img/introduceContainer3.gif"/></a></div>
            <div><span class="introduce-span">每天一个项目课，丰富你的项目经验</span></div>
          </div>
          <div class="introduce-unit col-sm-6 col-md-3">
            <div><a class="introduce-img"><img src="/static/img/introduceContainer4.gif"/></a></div>
            <div><span class="introduce-span">有效学习时间，真实记录你的代码生涯</span></div>
          </div>
        </div>
      </div>
    </div>
    <!--章节-->
    <div class="line-and-laboratory">
      <div class="container">
        <div class="clearfix text-center item-header">
          <span class="line"></span>
          <span class="text-center item-title">学习路径</span>
          <span class="line"></span>
        </div>
        <div class="tab-content">
          <div class="tab-pane clearfix active" id="study-line">


            <div class="col-xs-12 col-sm-6 col-md-4" v-for="item in paths">
              <a href="paths/show.html">
                <div class="path-item">
                  <div class="col-xs-5 col-sm-4 path-img">
                    <img :src="item.pic">
                  </div>
                  <div class="col-xs-7 col-sm-8">
                    <div class="path-name">{{item.name}}</div>
                    <div class="path-course-num">
                      <span>{{item.num}}</span>
                      门课程
                    </div>
                  </div>
                  <div class="desc-layer">
                    <div class="center">{{item.info}}
                    </div>
                  </div>
                </div>
              </a>
            </div>


          </div>
        </div>
      </div>
    </div>

    <!--    课程-->
    <div class="line-and-laboratory">
      <div class="container">
        <div class="clearfix text-center item-header">
          <span class="line"></span>
          <div class="text-center item-title">实验课程</div>
          <span class="line"></span>
        </div>
        <div class="clearfix courses">


          <div class="col-md-3 col-sm-6  courses" v-for="item in  courses">
            <a class="course-box" href="courses/show.html">
              <div class="sign-box">


                <i class="fa fa-star-o course-follow pull-right"
                   data-follow-url="/courses/1/follow"
                   data-unfollow-url="/courses/1/unfollow" style="display:none"></i>

              </div>
              <div class="course-img">

                <img alt="item.title" :src="item.pic">

              </div>

              <div class="course-body">
                <span class="course-title" data-toggle="tooltip" data-placement="bottom">{{item.title}}</span>
              </div>
              <div class="course-footer">
    			<span class="course-per-num pull-left">
                    <i class="fa fa-users"></i>

                    {{item.attention}}

    			</span>


              </div>
            </a>
          </div>


        </div>
        <div class="clearfix item-footer">
          <div class="pull-right watch-all">
<!--            <a href="courses/index.html">查看更多 ></a>-->
          </div>
        </div>
      </div>
    </div>


    <div class="modal fade" id="invite-user" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span
              class="sr-only">Close</span></button>
            <h4 class="modal-title">邀请好友，双方都可获赠实验豆！</h4>
          </div>
          <div class="modal-body">

            <p><h4><a href="#sign-modal" data-toggle="modal" data-sign="signin">登录</a>后邀请好友注册，您和好友将分别获赠3个实验豆！</h4></p>

            <div id="msg-modal"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" id="flash-message" tabindex="-1" role="dialog">
      <div class="modal-dialog" rolw="document">
      </div>
    </div>
    <div class="modal fade" id="modal-message" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span
              class="sr-only">Close</span></button>
            <h4 class="modal-title">注意</h4>
          </div>
          <div class="modal-body">
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
            <button type="button" class="btn btn-primary confirm" data-dismiss="modal">确定</button>
          </div>
        </div>
      </div>
    </div>

    <!--注册登录-->
    <div class="modal fade" id="sign-modal" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
          <button type="button" class="close-modal" data-dismiss="modal" aria-label="Close"><span aria-hidden="c1">&times;</span>
          </button>
          <div class="modal-body">
            <ul class="nav nav-tabs" role="tablist">
              <li role="presentation" class="active">
                <a href="#signin-form" aria-controls="signin-form" role="tab" data-toggle="tab">登录</a>
              </li>
              <li role="presentation">
                <a href="#signup-form" aria-controls="signup-form" role="tab" data-toggle="tab">注册</a>
              </li>
            </ul>
            <div class="tab-content">
              <div role="tabpanel" class="tab-pane active" id="signin-form">
                <form action="/login" method="post">
                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-addon">
                        <i class="fa fa-envelope" style="margin:0;"></i>
                      </div>
                      <input type="email" v-model="regForm.email" class="form-control" placeholder="请输入邮箱">
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-addon">
                        <i class="fa fa-lock" style="margin:0;"></i>
                      </div>
                      <input type="password" v-model="regForm.password" class="form-control" placeholder="请输入密码">
                    </div>
                  </div>
                  <!--                  <div class="form-inline verify-code-item" style="display:none;">-->
                  <!--                    <div class="form-group">-->
                  <!--                      <div class="input-group">-->
                  <!--                        <input type="text" name="captcha_v" class="form-control" placeholder="请输入验证码">-->
                  <!--                      </div>-->
                  <!--                    </div>-->
                  <!--                    <img class="verify-code" src="" source="https://www.shiyanlou.com/captcha.gif">-->
                  <!--                  </div>-->
                  <div class="form-group remember-login">
                    <input name="remember" type="checkbox" v-model="rememberPassword"> 下次自动登录
                    <a class="pull-right" href="reset_password/index.html">忘记密码？</a>
                  </div>
                  <div class="form-group">
                    <input class="btn btn-primary" name="submit" type="submit" @click="log" value="进入实验楼">
                  </div>
                  <div class="form-group widget-signin">
                    <span>快速登录</span>
                    <a href="/auth/qq?next="><i class="fa fa-qq"></i></a>
                    <a href="/api/login/"><i class="fa fa-weibo"></i></a>
                    <a href="/auth/weixin?next="><i class="fa fa-weixin"></i></a>
                    <a href="/auth/github?next="><i class="fa fa-github"></i></a>
                    <a href="/auth/renren?next="><i class="fa fa-renren"></i></a>
                  </div>
                  <div class="form-group error-msg">
                    <div class="alert alert-danger" role="alert"></div>
                  </div>
                </form>
              </div>
              <div role="tabpanel" class="tab-pane" id="signup-form">
                <!--                <form action="http://127.0.0.1:8000/reg" method="post">-->
                <div class="form-group">
                  <div class="input-group">
                    <div class="input-group-addon">
                      <i class="fa fa-envelope" style="margin:0;"></i>
                    </div>
                    <input type="email" v-model="regForm.email" class="form-control" placeholder="请输入邮箱">
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-group">
                    <div class="input-group-addon">
                      <i class="fa fa-lock" style="margin:0;"></i>
                    </div>
                    <input type="password" v-model="regForm.password" class="form-control" placeholder="请输入密码">
                  </div>
                </div>
                <div class="form-inline">
                  <div class="form-group">
                    <div class="input-group">
                      <input type="text" v-model="regForm.image_code" class="form-control" placeholder="请输入验证码">
                    </div>
                  </div>
                  <img class="get_msg_code"
                       src="/api/getimagecode/"
                       height="50" width="100"
                       onclick="this.src=this.src+'?'+Math.random()">
                  <!--                  <img class="verify-code" src="/api/getimagecode/" width="100" height="40">-->
                </div>
                <div class="form-group">
                  <input class="btn btn-primary" name="submit" type="submit" value="注册" @click="reg">
                </div>
                <div class="form-group agree-privacy">
                  注册表示您已经同意我们的<a href="privacy/index.html" target="_blank">隐私条款</a>
                </div>
                <div class="form-group widget-signup">
                  <span>快速注册</span>
                  <a href="/auth/qq?next="><i class="fa fa-qq"></i></a>
                  <a href="/auth/weibo?next="><i class="fa fa-weibo"></i></a>
                  <a href="/auth/weixin?next="><i class="fa fa-weixin"></i></a>
                  <a href="/auth/github?next="><i class="fa fa-github"></i></a>
                  <a href="/auth/renren?next="><i class="fa fa-renren"></i></a>
                </div>
                <div class="form-group error-msg">
                  <div class="alert alert-danger" role="alert"></div>
                </div>
                <!--                </form>-->
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>


    <div id="base-data"


         data-flash="false"


         data-is-login=false

         data-is-jwt=true
         data-socket-url="wss://comet.shiyanlou.com"
         data-msg-user=""
         data-msg-system=""
    >

    </div>
    <div id="jinja-data"
         data-post-url="/registercheck">
    </div>
    <footer></footer>
  </div>
</template>
<script>
    import header1 from '@/components/header1'
    import footer1 from '@/components/footer1'
    import right from '@/components/right'
    import {send} from '../../static/js/comm'

    export default {
        name: "index",
        components: {
            'header1': header1,
            'footer1': footer1,
            'right': right
        },
        data: function () {
            return {
                regForm: {
                    email: '',
                    password: '',
                    image_code: '',
                    c1: true

                },
                rememberPassword: false,
                courses: [],
                paths: [],
                isRouterAlive: true

            }
        },
        methods: {
            reg: function () {
                if (this.regForm.password.length < 8 || this.regForm.password.length > 20) {
                    alert('密码最少8位，最长20位')
                }
                var regEmail = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
                if (this.regForm.email === '') {
                    alert('邮箱为空')
                } else if (!regEmail.test(this.regForm.email)) {
                    alert('邮箱格式错误')
                }
                if (this.regForm.image_code.length !== 4) {
                    alert('验证码长度错误')
                }
                this.axios({
                    url: '/api/reg/',
                    method: 'post',
                    data: this.regForm
                }).then((res) => {
                    this.regForm.password = '';
                    this.regForm.image_code = '';
                    if (res.data.code == 200) {
                        alert(res.data.message)
                    } else {
                        alert(res.data.message)
                    }
                })
            },
            log: function () {
                alert(this.rememberPassword)
                if (this.regForm.password.length < 8 || this.regForm.password.length > 20) {
                    alert('密码最少8位，最长20位')
                }
                var regEmail = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
                if (this.regForm.email === '') {
                    alert('邮箱为空')
                } else if (!regEmail.test(this.regForm.email)) {
                    alert('邮箱格式错误')
                }
                this.regForm.username = this.regForm.email;
                this.axios({
                    url: '/api/login/',
                    method: 'post',
                    data: this.regForm
                }).then((res) => {
                    if (res.data.code == 200) {
                        alert(res.data.message)
                        localStorage.setItem('token', res.data.token);
                        localStorage.setItem('user_id', res.data.user_id);
                        localStorage.setItem('username', res.data.username);
                        if (this.rememberPassword == true) {
                            localStorage.setItem('password', this.regForm.password);
                        } else {
                            localStorage.setItem('password', 'null');
                        }
                        this.isRouterAlive = false;
                        this.$nextTick(() => (this.isRouterAlive = true))
                    } else {
                        alert(res.data.message)
                    }
                })
            },

        },
        mounted() {
            let code = this.$route.query.code;
            if (code != undefined) {
                alert(code)
            }
            send('/api/admin01/course/?limit=4', 'get').then((res) => {
                this.courses = res.data.dataList;
            });
            send('/api/admin01/path/?limit=12', 'get').then((res) => {
                this.paths = res.data.dataList;
            })
        }
    }
</script>

<style scoped>

</style>
