<template>
  <div id="course">
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


      <div class="row">
        <div class="col-md-9 layout-body">

          <div class="content">
            <div class="row course-cates">
              <div class="col-md-1 course-cates-title">类别：</div>
              <div class="col-md-11 course-cates-content">
                <a href="javascript:;" :class="{'active': member==-1}" @click="Setmember(-1)">全部</a>
                <a href="javascript:;" :class="{'active': member==0}" @click="Setmember(0)">免费</a>
                <!--                <a class="" @click="get_course_is_free(2)">限免</a>-->
                <div class="course-cates-vip ">
                  <a target="_blank" href="/vip"><img src="../../static/img/vip-icon.png"></a>
                  <a href="javascript:;" :class="{'active': member==1}" @click=" Setmember(1)">会员</a>
                </div>
              </div>
            </div>
            <div class="row course-cates">
              <div class="col-md-1 course-cates-title">标签：</div>
              <div class="col-md-11 course-cates-content">
                <a :class="{'active': tag==-1}" href="javascript:;" @click="Settag(-1)">全部</a>
                <a :class="{'active': tag==item.id}" href="javascript:;" v-for="item in tags" @click="Settag(item.id)">{{item.name}}</a>
              </div>
            </div>
          </div>
          <div class="content position-relative">
            <ul class="nav nav-tabs" role="tablist">
              <li :class="{'active': sale=='1'}"><a href="javascript:;" @click="Setsale(1)">已上线</a></li>
              <li :class="{'active': sale=='0'}"><a href="javascript:;" @click="Setsale(0)">即将上线</a>
              </li>
            </ul>
            <div class="clearfix"></div>
            <div class="courses-sort">
              <a href="javascript:;" :class="{'active': sort=='create_time'}" @click="Setsort('create_time')">最新</a>
              /
              <a href="javascript:;" :class="{'active': sort=='learn'}" @click="Setsort('-learn')">最热</a>
            </div>
            <div class="search-result"></div>
            <div class="row">
              <div class="col-md-4 col-sm-6  course" v-for="item in courses">
                <a href="#" class="course-box">
                  <div class="sign-box">
                    <i class="fa fa-star-o course-follow pull-right"
                       data-follow-url="/courses/63/follow"
                       data-unfollow-url="/courses/63/unfollow" style="display:none"></i>
                  </div>
                  <router-link :to="{'name':'courseDetail',query:{'id':item.id}}">
                    <div class="course-img">

                      <img :src="item.pic">

                    </div>
                    <div class="course-body">
                      <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="新手指南之玩转实验楼">{{item.title}}</span>
                    </div>
                  </router-link>
                  <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>
                {{item.learn}}
			</span>
                    <button class="course-bootcamp pull-right" @click="is_attention(item.id)"
                            v-if='clist.indexOf(item.id)==-1 &&user_id!=undefined'>关注
                    </button>
                    <button class="course-bootcamp pull-right" @click="is_attention(item.id)" v-else
                            v-show="user_id!=undefined">取消关注
                    </button>
                  </div>
                </a>
              </div>
            </div>
            <!--            <nav class="pagination-container">-->
            <!--              <ul class="pagination">-->

            <!--                <li class="disabled">-->
            <!--                  <a href="#" aria-label="Previous">-->
            <!--                    <span aria-hidden="true">上一页</span>-->
            <!--                  </a>-->
            <!--                </li>-->


            <!--                <li class="active">-->
            <!--                  <a href="/courses/?course_type=all&amp;tag=all&amp;fee=all&amp;page=1">1</a>-->
            <!--                </li>-->

            <!--              </ul>-->
            <!--            </nav>-->


          </div>

        </div>
        <right></right>
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
    <div class="modal fade" id="sign-modal" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
          <button type="button" class="close-modal" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span>
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
                    <a
                      href="https://ap  weibo.com/oauth2/authorize?client_id=2817332961&redirect_uri=http://127.0.0.1:8080/weibocallback###"><i
                      class="fa fa-weibo"></i></a>
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

    <footer1></footer1>
  </div>


</template>

<script>
    import header1 from '@/components/header1'
    import footer1 from '@/components/footer1'
    import right from '@/components/right'
    import {send} from '../../static/js/comm'


    export default {
        name: "cours",
        data: function () {
            return {
                courses: [],
                tags: [],
                tag: -1,
                sale: -1,
                member: -1,
                sort: 'learn',
                clist: [],
                paths: [],
                user_id: ''
            }
        },


        mounted() {
            this.tag = this.$route.params.tid;
            if (this.tag == undefined) {
                this.tag = -1
            }
            this.getCourse();
            this.user_id = localStorage.getItem('user_id');
            if (localStorage.getItem('user_id') != undefined) {
                this.getcoll();
            }
            send('/api/admin01/tag/', 'get').then((res) => {
                this.tags = res.data.tags;
            });
        },
        methods: {
            is_attention: function (id) {
                this.axios.post('/api/uploadcourse/', {
                    'id': id,
                    'user_id': localStorage.getItem('user_id')
                }).then((res) => {
                    if (res.data.code == 200) {
                        this.clist = res.data.clist
                        this.getCourse()
                        this.getcoll()
                    }

                })

            },
            getcoll: function () {
                this.axios.get('/api/uploadcourse/?user_id=' + localStorage.getItem('user_id')).then((res) => {
                    if (res.data.code == 200) {
                        this.clist = res.data.clist
                        console.log(res.data.clist)
                    }
                })
            }

            ,
            getCourse: function () {
                send('/api/showCourse/?tag=' + this.tag + '&sale=' + this.sale + '&member=' + this.member + '&sort=' + this.sort, 'get').then((res) => {
                    this.courses = res.data.dataList;
                });
            },
            Setmember: function (member) {
                this.member = member;
                this.getCourse()
            },
            Setsale: function (sale) {
                this.sale = sale;
                this.getCourse()
            },
            Settag: function (tag) {
                this.tag = tag;
                this.getCourse()
            },
            Setsort: function (sort) {
                this.sort = sort;
                this.getCourse()
            },
        },
        components: {
            header1: header1,
            footer1: footer1,
            right: right
        },
    }
</script>

<style scoped>

</style>
