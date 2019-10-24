<template>
  <div id="stage">
    <header1></header1>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="Lei Shi">
    <meta http-equiv="Cache-Control" content="o-transform">
    <meta http-equiv="Cache-Control" content="no-siteapp">
    <meta name="csrf-token" content="1483780974##87f89328c5616669f00302a263fe9061bb852818">
    <title>全部 - 课程 - 实验楼</title>
    <meta content="实验楼课程分为基础课和项目课,内容涵盖了Linux、Python、Java、C语言、Ruby、Android、IOS开发、大数据、信息安全等IT技术领域。" name="description">
    <meta content="实验楼课程,IT培训课程,IT实训课程,IT在线课程,all" name="keywords">
    <meta content="实验楼,琛石科技" name="author">

    <div class="container layout layout-margin-top">

      <ol class="breadcrumb">
        <li>
          <router-link :to="{'name':'path'}">学习路径</router-link>
        </li>
        <li class="active">{{pathData.name}}</li>
      </ol>

      <div class="row">
        <div class="col-md-9 layout-body">

          <div class="content" style="padding:0px">
            <div class="path-description" style="margin:0px">
              <div class="path-desc-top clearfix"
                   :style="{backgroundImage:'url(' + pic + ')', backgroundRepeat:'no-repeat', backgroundSize: 'cover'}">
                <!--                   :style="{background:url(pathData.pic)}">-->

                <div class="name-total-box clearfix">
                  <div class="col-md-6 col-sm-6 col-md-offset-1 path-name">
                    <h4>{{pathData.name}}</h4>
                  </div>
                  <div class="col-md-3 col-sm-6 col-md-offset-1 path-total-courses">
                    <span class="total-courses-box">课程 <span class="num">{{pathData.num}}</span></span>
                  </div>
                </div>
                <div class="col-md-10 col-md-offset-1 path-desc-text">{{pathData.info}}
                </div>
              </div>
              <div class="path-desc-btm">
                <div class="col-sm-12 col-md-4 clearfix learn-time-div">
                  <!--                  <div class="col-md-12 text-left need-learn-time">预计需要 <span class="num">30</span> 小时学习</div>-->
                </div>
                <div class="col-sm-12 col-md-8  clearfix text-right" style="padding-top:0px">
                  <div class="col-xs-12">

                    <a class="btn btn-path-operation btn-join-path" data-sign="signin" href="javascript:;"
                       data-toggle="modal" v-show="user_id !=undefined" @click="joinPath">加入路径</a>

                    <p style="font-size:10px;margin-top:5px">加入获得路径课程更新提醒</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="content">
            <ul class="nav nav-tabs" role="tablist">
              <li role="presentation" class="active">
                <a href="#path-details" aria-controls="path-details" role="tab" data-toggle="tab">路径详情</a>
              </li>
              <li role="presentation">
                <a href="#path-comments" aria-controls="path-comments" role="tab" data-stat="path_comments"
                   data-toggle="tab">路径评论(<span class="comments-count">0</span>)</a>
              </li>
            </ul>
            <div class="tab-content">
              <div role="tabpanel" class="tab-pane path-details active" id="path-details">
                <!--                <a href="/courses/63" class="btn start-btn">开始学习</a>-->
                <div class="details-box" v-for="item in pathData.stageList">
                  <div class="clearfix text-center path-title-box">
                    <span class="line hidden-xs"></span>
                    <span>{{item.name}}</span>
                    <span class="line hidden-xs"></span>
                  </div>
                  <div class="row">
                    <div class="col-md-4 col-sm-6  course" v-for="i in item.courseList">
                      <router-link :to="{'name':'courseDetail',params:{'id':i.id}}" class="course-box">
                        <div class="sign-box">

                          <i class="fa fa-star-o course-follow pull-right"
                             data-follow-url="/courses/63/follow"
                             data-unfollow-url="/courses/63/unfollow" style="display:none"></i>
                        </div>
                        <div class="course-img">

                          <img :src="i.pic">

                        </div>

                        <div class="course-body">
                          <span class="course-title" data-toggle="tooltip" data-placement="bottom" :title="i.title">{{i.title}}</span>
                        </div>
                        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                {{i.learn}}

			</span>


                        </div>
                      </router-link>
                    </div>
                  </div>


                </div>
                <!--                <div class="btn end-pin">完成学习</div>-->
              </div>
              <div role="tabpanel" class="tab-pane path-comment" id="path-comments">
                <div class="comment-box">
                  <div class="comment-form">

                    <div class="comment-form-unlogin">
                      请
                      <a href="#sign-modal" data-toggle="modal" data-sign="signin"> 登录 </a>
                      后发表评论
                    </div>

                  </div>
                  <div class="comment-title">最新评论</div>
                  <div class="comment-list"></div>
                  <div class="pagination-container"></div>
                </div>
              </div>
            </div>
          </div>

        </div>
        <right></right>


        <!--        右侧-->

      </div>
    </div>
    <!--    ok-->

    <div class="modal fade" id="invite-user" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span
              class="sr-only">Close</span></button>
            <h4 class="modal-title">邀请好友，双方都可获赠实验豆！</h4>
          </div>
          <div class="modal-body">
            <h4><a href="#sign-modal" data-toggle="modal" data-sign="signin">登录</a>后邀请好友注册，您和好友将分别获赠3个实验豆！</h4>

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


    <!--    <div class="modal fade" id="sign-modal" tabindex="-1" role="dialog">-->
    <!--      <div class="modal-dialog modal-sm" role="document">-->
    <!--        <div class="modal-content">-->
    <!--          <button type="button" class="close-modal" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span>-->
    <!--          </button>-->
    <!--          <div class="modal-body">-->
    <!--            <ul class="nav nav-tabs" role="tablist">-->
    <!--              <li role="presentation" class="active">-->
    <!--                <a href="#signin-form" aria-controls="signin-form" role="tab" data-toggle="tab">登录</a>-->
    <!--              </li>-->
    <!--              <li role="presentation">-->
    <!--                <a href="#signup-form" aria-controls="signup-form" role="tab" data-toggle="tab">注册</a>-->
    <!--              </li>-->
    <!--            </ul>-->
    <!--            <div class="tab-content">-->
    <!--              <div role="tabpanel" class="tab-pane active" id="signin-form">-->
    <!--                <form action="/login" method="post">-->
    <!--                  <div class="form-group">-->
    <!--                    <div class="input-group">-->
    <!--                      <div class="input-group-addon">-->
    <!--                        <i class="fa fa-envelope" style="margin:0;"></i>-->
    <!--                      </div>-->
    <!--                      <input type="email" name="login" class="form-control" placeholder="请输入邮箱">-->
    <!--                    </div>-->
    <!--                  </div>-->
    <!--                  <div class="form-group">-->
    <!--                    <div class="input-group">-->
    <!--                      <div class="input-group-addon">-->
    <!--                        <i class="fa fa-lock" style="margin:0;"></i>-->
    <!--                      </div>-->
    <!--                      <input type="password" name="password" class="form-control" placeholder="请输入密码">-->
    <!--                    </div>-->
    <!--                  </div>-->
    <!--                  <div class="form-inline verify-code-item" style="display:none;">-->
    <!--                    <div class="form-group">-->
    <!--                      <div class="input-group">-->
    <!--                        <input type="text" name="captcha_v" class="form-control" placeholder="请输入验证码">-->
    <!--                      </div>-->
    <!--                    </div>-->
    <!--                    <img class="verify-code" src="" source="https://www.shiyanlou.com/captcha.gif">-->
    <!--                  </div>-->
    <!--                  <div class="form-group remember-login">-->
    <!--                    <input name="remember" type="checkbox" value="y"> 下次自动登录-->
    <!--                    <a class="pull-right" href="../reset_password/index.html">忘记密码？</a>-->
    <!--                  </div>-->
    <!--                  <div class="form-group">-->
    <!--                    <input class="btn btn-primary" name="submit" type="submit" value="进入实验楼">-->
    <!--                  </div>-->
    <!--                  <div class="form-group widget-signin">-->
    <!--                    <span>快速登录</span>-->
    <!--                    <a href="/auth/qq?next="><i class="fa fa-qq"></i></a>-->
    <!--                    <a-->
    <!--                      href="https://ap  weibo.com/oauth2/authorize?client_id=2817332961&redirect_uri=http://127.0.0.1:8080/weibocallback###"><i-->
    <!--                      class="fa fa-weibo"></i></a>-->
    <!--                    <a href="/auth/weixin?next="><i class="fa fa-weixin"></i></a>-->
    <!--                    <a href="/auth/github?next="><i class="fa fa-github"></i></a>-->
    <!--                    <a href="/auth/renren?next="><i class="fa fa-renren"></i></a>-->
    <!--                  </div>-->
    <!--                  <div class="form-group error-msg">-->
    <!--                    <div class="alert alert-danger" role="alert"></div>-->
    <!--                  </div>-->
    <!--                </form>-->
    <!--              </div>-->
    <!--              <div role="tabpanel" class="tab-pane" id="signup-form">-->
    <!--                <form action="/register" method="post">-->
    <!--                  <div class="form-group">-->
    <!--                    <div class="input-group">-->
    <!--                      <div class="input-group-addon">-->
    <!--                        <i class="fa fa-envelope" style="margin:0;"></i>-->
    <!--                      </div>-->
    <!--                      <input type="email" name="email" class="form-control" placeholder="请输入邮箱">-->
    <!--                    </div>-->
    <!--                  </div>-->
    <!--                  <div class="form-group">-->
    <!--                    <div class="input-group">-->
    <!--                      <div class="input-group-addon">-->
    <!--                        <i class="fa fa-lock" style="margin:0;"></i>-->
    <!--                      </div>-->
    <!--                      <input type="password" name="password" class="form-control" placeholder="请输入密码">-->
    <!--                    </div>-->
    <!--                  </div>-->
    <!--                  <div class="form-inline">-->
    <!--                    <div class="form-group">-->
    <!--                      <div class="input-group">-->
    <!--                        <input type="text" name="captcha_v" class="form-control" placeholder="请输入验证码">-->
    <!--                      </div>-->
    <!--                    </div>-->
    <!--                    <img class="verify-code" src="" source="https://www.shiyanlou.com/captcha.gif">-->
    <!--                  </div>-->
    <!--                  <div class="form-group">-->
    <!--                    <input class="btn btn-primary" name="submit" type="submit" value="注册">-->
    <!--                  </div>-->
    <!--                  <div class="form-group agree-privacy">-->
    <!--                    注册表示您已经同意我们的<a href="../privacy/index.html" target="_blank">隐私条款</a>-->
    <!--                  </div>-->
    <!--                  <div class="form-group widget-signup">-->
    <!--                    <span>快速注册</span>-->
    <!--                    <a href="/auth/qq?next="><i class="fa fa-qq"></i></a>-->
    <!--                    <a href="/auth/weibo?next="><i class="fa fa-weibo"></i></a>-->
    <!--                    <a href="/auth/weixin?next="><i class="fa fa-weixin"></i></a>-->
    <!--                    <a href="/auth/github?next="><i class="fa fa-github"></i></a>-->
    <!--                    <a href="/auth/renren?next="><i class="fa fa-renren"></i></a>-->
    <!--                  </div>-->
    <!--                  <div class="form-group error-msg">-->
    <!--                    <div class="alert alert-danger" role="alert"></div>-->
    <!--                  </div>-->
    <!--                </form>-->
    <!--              </div>-->
    <!--            </div>-->
    <!--          </div>-->
    <!--        </div>-->
    <!--      </div>-->
    <!--    </div>-->


    <div id="base-data"


         data-flash="false"


         data-is-login=false

         data-is-jwt=true
         data-socket-url="wss://comet.shiyanlou.com"
         data-msg-user=""
         data-msg-system=""
    ></div>

    <div id="jinja-data"
         data-loginurl="/login"
         data-private-course-url="/courses/join"
         data-site-type="0"

    ></div>

    <footer1></footer1>
  </div>


</template>

<script>
    import header1 from '@/components/header1'
    import footer1 from '@/components/footer1'
    import right from '@/components/right'
    import {send} from '../../static/js/comm'
    // import Right from "./right";


    export default {
        name: "stage",
        data: function () {
            return {
                path_id: 0,
                pathData: {},
                pic: '',
                user_id: localStorage.getItem('user_id')
            }
        },


        mounted() {
            this.path_id = this.$route.query.id;

            // alert(this.path_id);
            send('/api/path/?id=' + this.path_id, 'get').then((res) => {
                if (res.data.code == 200) {
                    this.pathData = res.data.pathData;
                    this.pic = this.pathData.pic.replace('\\', '\\\\')
                } else {
                    this.$router.push({name: 'path1'})
                }
            }).catch((err) => {
                this.$router.push({name: 'path1'})
            })
        },
        methods: {
            joinPath: function () {
                send('/api/mypath/', 'post', {'path_id': this.path_id, 'user_id': this.user_id}).then((res) => {
                    if (res.data == 200) {
                        alert('添加成功')
                    } else {
                        alert(res.data.message)
                    }
                })
            },
            getPath: function () {
                send('/api/admin01/path/', 'get').then((res) => {
                    this.paths = res.data.dataList;
                });
            },
        },
        components: {
            right: right,
            header1: header1,
            footer1: footer1
        },
    }
</script>

<style scoped>
  /*.backg{*/
  /*  background-image: ;*/
  /*}*/
</style>
