<template>
  <div>
    <header1></header1>

    <div class="container layout layout-margin-top">

      <div class="row">
        <div class="col-md-9 layout-body">


          <div class="content position-relative">
            <ul class="nav nav-tabs" role="tablist">
              <li :class="{'active':online_on}"><a href="javascript:void(0);" @click="choose_online(0)"
                                                   :value="0">已上线</a></li>
              <li :class="{'active':online_off}"><a href="javascript:void(0);" @click="choose_online(1)"
                                                    :value="1">即将上线</a></li>
            </ul>
            <div class="clearfix"></div>
            <div class="courses-sort">
              <a href="javascript:void(0);" @click="changelist('learn')" :value="1">最新</a>
              /
              <a href="javascript:void(0);" @click="changelist('attention')" :value="0">最热</a>
            </div>

            <div class="search-result"></div>

            <div class="row">
              <!-- 课程展示 -->
              <div class="col-md-4 col-sm-6  course" v-for="i in courselist" :key="i">
                <a :href="'/course_detail?cid='+i.id" class="course-box">
                <!-- <router-link class="course-box" :to="{name:'course_detail',params:{'cid':i.id}}"> -->
                <div class="sign-box">
                  <i class="fa fa-star-o course-follow pull-right">
                    <!--                    data-follow-url="/courses/708/follow"-->
                    <!--                    data-unfollow-url="/courses/708/unfollow"  style="display:none"  >-->
                  </i>

                </div>
                <div class="course-img">

                  <img :alt="i.title" :src="i.pic">

                </div>

                <div class="course-body">
                  <span class="course-title" data-toggle="tooltip" data-placement="bottom"
                        title="Python 3 实现 Markdown 解析器">{{i.title}}</span>
                </div>
                <div class="course-footer">
                <span class="course-per-num pull-left">
                    <i class="fa fa-users"></i>{{i.attention}}</span>


                  <span class="course-money pull-right">会员</span>


                </div>
                </a>
                <!-- </router-link> -->
              </div>


            </div>


            <nav class="pagination-container">
              <ul class="pagination">

                <li class="disabled">
                  <a href="#" aria-label="Previous">
                    <span aria-hidden="true">上一页</span>
                  </a>
                </li>


                <li class="active">
                  <a href="">1</a>
                </li>


                <li class="">
                  <a href="">2</a>
                </li>


                <li class="">
                  <a aria-label="Next" href="">
                    <span aria-hidden="true">下一页</span>
                  </a>
                </li>

              </ul>
            </nav>


          </div>

        </div>

        <div class="col-md-3 layout-side">


          <div class="panel panel-default panel-userinfo">
            <div class="panel-body body-userinfo">
              <div class="media userinfo-header">
                <div class="media-left">
                  <div class="user-avatar">

                    <a class="avatar" href="#sign-modal" data-toggle="modal" data-sign="signin">
                      <img class="circle" src="/static/img/logo-grey.png">
                    </a>

                  </div>
                </div>
                <div class="media-body">

                  <span class="media-heading username">欢迎来到实验楼</span>
                  <p class="vip-remain">做实验，学编程</p>

                </div>
              </div>

              <div class="row userinfo-data">

                <hr>
                <div class="btn-group-lr">
                  <a href="#sign-modal" type="button" class="btn btn-success col-md-5 col-xs-6 login-btn"
                     data-toggle="modal" data-sign="signin">登录</a>
                  <a href="#sign-modal" type="button"
                     class="btn btn-success col-md-5 col-xs-6 col-md-offset-1 register-btn" data-toggle="modal"
                     data-sign="signup">注册</a>
                </div>

              </div>

              <div class="userinfo-footer row">
                <div class="col-md-6 col-xs-6 pos-left">

                  <a href="#sign-modal" data-toggle="modal" data-sign="signin"><span
                    class="glyphicon glyphicon-bookmark"></span> 加入私有课</a>

                </div>
                <div class="col-md-6 col-xs-6 pos-right">
                  <a href="/contribute" target="_blank"><span class="glyphicon glyphicon-send"></span> 我要投稿</a>
                </div>

                <div id="join-private-course" class="modal fade words-ctrl" tabindex="-1" role="dialog">
                  <div class="modal-dialog" role="document">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h4 class="modal-title">加入私有课</h4>
                      </div>
                      <div class="modal-body">
                        <div style="margin:15px 0; font:16px;">输入教师提供的私有课程码可以加入教师的私有课程。</div>
                        <form id="private-course-form" method="POST" action="/courses/join">
                          <div class="form-group">
                            <label for="code">邀请码</label>
                            <input class="form-control" id="code" name="code" type="text" value="">
                            <input name="_csrf_token" type=hidden
                                   value="1483780974##87f89328c5616669f00302a263fe9061bb852818">
                          </div>
                        </form>

                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                        <button type="button" class="btn btn-primary"
                                onclick="document.getElementById('private-course-form').submit();">确定
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>


          <div class="sidebox">

            <div class="sidebox-header">
              <h4 class="sidebox-title">最热路径</h4>
            </div>
            <div class="sidebox-body course-content side-list-body">
              <a href="/paths/python"><img style="width:25px;height:25px" src="/static/img/1471513769430.png"> Python
                研发工程师</a>
              <a href="/paths/bigdata"><img style="width:25px;height:25px" src="/static/img/1471513926288.png">
                大数据工程师</a>
              <a href="/paths/cpp"><img style="width:25px;height:25px" src="/static/img/1471513793360.png"> C++
                研发工程师</a>
              <a href="/paths/security"><img style="width:25px;height:25px" src="/static/img/1471513867033.png"> 信息安全工程师</a>
              <a href="/paths/linuxsys"><img style="width:25px;height:25px" src="/static/img/1471514004752.png"> Linux
                运维工程师</a>
            </div>

          </div>

          <div class="side-image side-qrcode">
            <img src="/static/img/ShiyanlouQRCode.png">
            <div class="side-image-text">关注公众号，手机看教程</div>
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

            <p>
            <h4><a href="#sign-modal" data-toggle="modal" data-sign="signin">登录</a>后邀请好友注册，您和好友将分别获赠3个实验豆！</h4>
            </p>

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
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true"></span><span
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


    <div class="modal fade" id="sign-modal" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
          <button type="button" class="close-modal" data-dismiss="modal" aria-label="Close"><span
            aria-hidden="true"></span></button>
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
                      <input type="email" name="login" class="form-control" placeholder="请输入邮箱">
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-addon">
                        <i class="fa fa-lock" style="margin:0;"></i>
                      </div>
                      <input type="password" name="password" class="form-control" placeholder="请输入密码">
                    </div>
                  </div>
                  <div class="form-inline verify-code-item" style="display:none;">
                    <div class="form-group">
                      <div class="input-group">
                        <input type="text" name="captcha_v" class="form-control" placeholder="请输入验证码">
                      </div>
                    </div>
                    <img class="verify-code" src="" source="https://www.shiyanlou.com/captcha.gif">
                  </div>
                  <div class="form-group remember-login">
                    <input name="remember" type="checkbox" value="y"> 下次自动登录
                    <a class="pull-right" href="../reset_password/index.html">忘记密码？</a>
                  </div>
                  <div class="form-group">
                    <input class="btn btn-primary" name="submit" type="submit" value="进入实验楼">
                  </div>
                  <div class="form-group widget-signin">
                    <span>快速登录</span>
                    <a href="/auth/qq?next="><i class="fa fa-qq"></i></a>
                    <a href="/auth/weibo?next="><i class="fa fa-weibo"></i></a>
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
                <form action="/register" method="post">
                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-addon">
                        <i class="fa fa-envelope" style="margin:0;"></i>
                      </div>
                      <input type="email" name="email" class="form-control" placeholder="请输入邮箱">
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-addon">
                        <i class="fa fa-lock" style="margin:0;"></i>
                      </div>
                      <input type="password" name="password" class="form-control" placeholder="请输入密码">
                    </div>
                  </div>
                  <div class="form-inline">
                    <div class="form-group">
                      <div class="input-group">
                        <input type="text" name="captcha_v" class="form-control" placeholder="请输入验证码">
                      </div>
                    </div>
                    <img class="verify-code" src="" source="https://www.shiyanlou.com/captcha.gif">
                  </div>
                  <div class="form-group">
                    <input class="btn btn-primary" name="submit" type="submit" value="注册">
                  </div>
                  <div class="form-group agree-privacy">
                    注册表示您已经同意我们的<a href="../privacy/index.html" target="_blank">隐私条款</a>
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
                </form>
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
    ></div>


    <div id="jinja-data"
         data-loginurl="/login"
         data-private-course-url="/courses/join"
         data-site-type="0"
    ></div>

    <!-- <script src="../app/dest/course/index.js?=2016121272249"></script> -->
    <footer1></footer1>

  </div>
</template>
<script>
    import header1 from "./header1";
    import footer1 from "./footer1";
    import {send} from '../../static/js/comm'

    export default {
        name: "redisearch",
        components: {
            'header1': header1,
            'footer1': footer1
        },
        data() {
            return {
                courselist: '',
                member_id: 0,
                course: '',
                online: 0,
                change_id: -1,
                online_on: true,
                online_off: false,
                pathlist: '',
                path: -1,
                all: true,
                selectdata: {},
                key: ''

            }
        },
        methods: {
            on_submit: function () {
                // send('/api/shop/courselist/','post',{'member':this.member_id,'tag_id':this.tag_id,'online':this.online,'change_id':this.change_id,'path_id':this.path}).then((res)=> {
                send('/api/shop/redis_search/', 'post', {
                    'tag': this.tag_id,
                    'online': this.online,
                    'change_id': this.change_id,
                    'path': this.path
                }).then((res) => {
                    console.log(res)
                    this.courselist = res.data.course
                    let selectdata = {}
                    for (var i = 0; i < this.courselist.length; i++) {
                        selectdata.push(i.name)

                    }
                    this.selectdata = selectdata
                    console.log(this.selectdata)

                })

            },
            choose_path: function (val) {
                alert(val)
                this.path = val
                this.on_submit()
            },
            changelist: function (val) {
                alert(val)
                this.change_id = val
                this.on_submit()
            },
            choose_online: function (val) {
                alert(val)
                this.online = val
                if (val == '0') {
                    this.online_on = true
                    this.online_off = false
                } else {
                    this.online_off = true
                    this.online_on = false
                }

                this.on_submit()
            },
            choose_tag: function (val) {
                alert(val)
                this.tag_id = val
                this.on_submit()
            }
        },
        mounted() {
            // alert(this.$route.query.search)

            send('/api/admin01/redis_search/?key=' + this.$route.query.search, 'get', {}).then((res) => {
                if (res.data.code == 200) {
                    console.log(res.data.course)
                    this.courselist = res.data.course


                } else {
                    alert('连接失败')
                }
            })
            // this.$router.go('http://localhost:8080/redisearch?key=python')
        }
    }
</script>
