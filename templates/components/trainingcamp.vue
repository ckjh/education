<template>
  <div id="BootCamp">

    <header1></header1>
    <div class="bootcamp-description layout-no-margin-top">
      <div>
        <h1>来一场高效又实战的训练</h1>
        <h4>资深工程师指导学习，实战中融会贯通IT技术</h4>
        <button class="btn">立即加入</button>
      </div>
    </div>

    <div class="bootcamp-features">
      <div class="container">
        <div class="row">
          <div class="col-md-3">
            <img src="../../static/img/bootcamp-project.png">
            <div class="bootcamp-features-description">
              <span>优秀项目</span>
              <span>专注实战</span>
            </div>
          </div>
          <div class="col-md-3">
            <img style=" padding-left: 24px;" src="../../static/img/bootcamp-teacher.png">
            <div class="bootcamp-features-description">
              <span>技术大牛</span>
              <span>有问必答</span>
            </div>
          </div>
          <div class="col-md-3">
            <img src="../../static/img/bootcamp-comment.png">
            <div class="bootcamp-features-description">
              <span>实验报告</span>
              <span>悉心点评</span>
            </div>
          </div>
          <div class="col-md-3">
            <img src="../../static/img/bootcamp-certificate.png">
            <div class="bootcamp-features-description">
              <span>完成课程</span>
              <span>获得证书</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="bootcamp-courses">
      <div class="container">
        <div class="bootcamp-courses-header">
          <h4 class="bootcamp-courses-title">训练营课程</h4>
          <div class="bootcamp-courses-description">
            动手实践，激发创新实力
          </div>
        </div>

        <div class="bootcamp-courses-body">

          <div class="media bootcamp-courses-item" v-for="(i,index) in bootcampList" :key="index">
            <div class="media-left bootcamp-courses-media">
              <img class="media-object" :src="i.pic">
            </div>
            <div class="media-body bootcamp-courses-body">
              <div class="bootcamp-courses-info">
                <h4 class="media-heading"><span>{{i.online}}</span>{{i.title}}</h4>
                <div><p>{{i.info}}</p></div>
                <!--<div>推荐先学：<a href="https://www.shiyanlou.com/courses/1" target="_blank">Linux基础入门</a> </div>-->
                <div>
<!--                  <p><a class="tagStyle2">Kali</a><a class="tagStyle2">渗透测试</a><a class="tagStyle2">Linux</a></p>-->
                </div>
              </div>
              <div class="bootcamp-courses-subscribe">
                <div class="pull-right bootcamp-courses-order">
                  <div class="pull-left">
                    <span style="margin-bottom: -8px;">￥{{i.prices[2].discoun_price}}</span>
                    <span class="member-price" data-container="body" data-toggle="popover" data-placement="top"
                          data-original-title="会员优惠" data-html="true"
                          data-content="普通会员(<span class='price-number'>8折</span>)：<span class='price-number'>￥103.2</span><br>高级会员(<span class='price-number'>5折</span>)：<span class='price-number'>￥64.5&nbsp;&nbsp;</span>"><a
                      href="#" title="">会员最低{{i.prices[0].discount}}折</a></span>
                  </div>
                  <a class="btn pull-right" :href='"/courseDetail?id="+i.id'>查看详情</a>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
    <div class="bootcamp-faq">
      <div class="container">
        <div class="bootcamp-faq-header">
          <h4 class="bootcamp-faq-title">训练营FAQ</h4>
        </div>
        <div class="bootcamp-faq-body">
          <div class="bootcamp-faq-question">
            WHAT：实验楼训练营是什么？
          </div>
          <div class="bootcamp-faq-answer">
            <img src="../../static/img/bootcamp-answer.png">：训练营是一系列有教师服务（有问必答，实验报告点评等）的实验课。您将在教师指导下，在实验楼中完成一个可上线运行的产品原型或一系列编程任务，项目实战中融会贯通2-3门IT技术及开发流程。
          </div>
          <div class="bootcamp-faq-question">
            WHY：为什么选择实验楼训练营课程？
          </div>
          <div class="bootcamp-faq-answer">
            <img src="../../static/img/bootcamp-answer.png">：实战，实战，实战！课程教师是具备多年研发经验的资深工程师，课程选题来自优秀的开源技术或仿知名网站。非常适合已学基础技术却迷茫不知道如何运用的同学，零基础的同学可按课程要求学习推荐的先学课程。
          </div>
          <div class="bootcamp-faq-question">
            HOW：训练营课程学习流程是怎样的？
          </div>
          <div class="bootcamp-faq-answer">
            <img src="../../static/img/bootcamp-answer.png">：按实验文档依次完成实验，公开实验报告，实验中的问题随时在问答中提交，教师24小时内回复问答。完成所有实验并认真提交实验报告，可获得GOOD或PASS课程证书。
          </div>
        </div>
        <div class="bootcamp-faq-footer">
          <a class="bootcamp-faq-more" href="/questions/918" target="_blank">更多疑问，查看这里>></a>
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

            <div><h4><a href="#sign-modal" data-toggle="modal" data-sign="signin">登录</a>后邀请好友注册，您和好友将分别获赠3个实验豆！</h4>
            </div>

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
    <footer1></footer1>
  </div>
</template>

<script>
    import header1 from '@/components/header1'
    import footer1 from '@/components/footer1'
    import {send, sendToken} from '../../static/js/comm'


    export default {
        name: "BootCamp",
        data() {
            return {
                bootcampList: [],
            }
        },
        components: {
            header1: header1,
            footer1: footer1,
        },
        mounted() {
            send('/api/showCourse/?tag=99' + '&sale=-1&member=-1&sort=learn', 'get').then((res) => {
                this.bootcampList = res.data.dataList;
            });
        }
    }
</script>

<style scoped>

</style>
