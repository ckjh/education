<template>
  <div id="right">
    <div class="col-md-3 layout-side">
      <a class="btn side-btn" href="#sign-modal" @click="shows">我要发帖</a>


      <div class="sidebox">
        <div class="sidebox-header">
          <h4 class="sidebox-title">最热路径</h4>
        </div>
        <div class="sidebox-body course-content side-list-body" style="text-align:left">
<!--          <router-link :to="{'name':'stage',query:{'id':item.id}}">-->
          <a :href='"/stage?id="+item.id' v-for="item in paths"><img style="width:25px;height:25px" :src="item.pic">
            {{item.name}}</a>
        </div>
      </div>

      <!--      <div class="side-image side-qrcode">-->
      <!--        <img src="../../static/img/ShiyanlouQRCode.png">-->
      <!--        <div class="side-image-text">关注公众号，手机看教程</div>-->
      <!--      </div>-->

    </div>
    <div class="modal fade askquestion-modal" id="askquestion" tabindex="-1" role="dialog">
      <div class="modal-dialog" role=document>
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
            <h4 class="modal-title">发帖</h4>
          </div>
          <div class="modal-body words-ctrl">

            <fuwenben v-on:listentochildevents='showMesfromchild'></fuwenben>

          </div>
          <div class="modal-footer">      <!--../../static/img/senior-vip-icon.png-->

            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
            <!--            <button type="button" class="submit-question btn btn-primary" data-dismiss="modal" @click="adddiscuss">-->
            <!--              发表讨论-->
            <!--            </button>-->
          </div>
        </div>
      </div>
    </div>


    <div class="col-md-3 layout-side" style="float: right">

      <!--      <div class="panel panel-default panel-userinfo">-->
      <!--        <div class="panel-body body-userinfo">-->
      <!--          <div class="media userinfo-header">-->
      <!--            <div class="media-left">-->
      <!--              <div class="user-avatar">-->

      <!--                <a class="avatar" href="#sign-modal" data-toggle="modal" data-sign="signin">-->
      <!--                  <img class="circle" src="../../static/img/logo-grey.png">-->
      <!--                </a>-->

      <!--              </div>-->
      <!--            </div>-->
      <!--            <div class="media-body">-->

      <!--              <span class="media-heading username">欢迎来到实验楼</span>-->
      <!--              <p class="vip-remain">做实验，学编程</p>-->

      <!--            </div>-->
      <!--          </div>-->

      <!--          <div class="row userinfo-data" v-if="false">-->

      <!--            <hr>-->
      <!--            <div class="btn-group-lr">-->
      <!--              <a href="#sign-modal" type="button" class="btn btn-success col-md-5 col-xs-6 login-btn"-->
      <!--                 data-toggle="modal" data-sign="signin">登录</a>-->
      <!--              <a href="#sign-modal" type="button"-->
      <!--                 class="btn btn-success col-md-5 col-xs-6 col-md-offset-1 register-btn" data-toggle="modal"-->
      <!--                 data-sign="signup">注册</a>-->
      <!--            </div>-->

      <!--          </div>-->

      <!--          <div class="userinfo-footer row">-->
      <!--            <div class="col-md-6 col-xs-6 pos-left">-->

      <!--              <a href="#sign-modal" data-toggle="modal" data-sign="signin"><span-->
      <!--                class="glyphicon glyphicon-bookmark"></span> 加入私有课</a>-->

      <!--    </div>-->


      <!--            <div id="join-private-course" class="modal fade words-ctrl" tabindex="-1" role="dialog">-->
      <!--              <div class="modal-dialog" role="document">-->
      <!--                <div class="modal-content">-->
      <!--                  <div class="modal-header">-->
      <!--                    <h4 class="modal-title">加入私有课</h4>-->
      <!--                  </div>-->
      <!--                  <div class="modal-body">-->
      <!--                    <div style="margin:15px 0; font:16px;">输入教师提供的私有课程码可以加入教师的私有课程。</div>-->
      <!--                    <form id="private-course-form" method="POST" action="/courses/join">-->
      <!--                      <div class="form-group">-->
      <!--                        <label for="code">邀请码</label>-->
      <!--                        <input class="form-control" id="code" name="code" type="text" value="">-->
      <!--                        <input name="_csrf_token" type=hidden-->
      <!--                               value="1483796689##5dfe74a8992e829e903291b65bbbdabafa60f4e1">-->
      <!--                      </div>-->
      <!--                    </form>-->

      <!--                  </div>-->
      <!--                  <div class="modal-footer">-->
      <!--                    <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>-->
      <!--                    <button type="button" class="btn btn-primary"-->
      <!--                            onclick="document.getElementById('private-course-form').submit();">确定-->
      <!--                    </button>-->
      <!--                  </div>-->
      <!--                </div>-->
      <!--              </div>-->
      <!--            </div>-->
      <!--          </div>-->
      <!--        </div>-->
      <!--      </div>-->
      <div class="sidebox">
        <a target="_blank" href="http://wpa.qq.com/msgrd?v=3&uin=983835821&site=qq&menu=yes"><img border="0"
                                                                                                  src="http://wpa.qq.com/pa?p=2:983835821:52"
                                                                                                  alt="点我咨询"
                                                                                                  title="点我咨询"/>点我咨询</a>
        <div class="sidebox-header">
          <h4 class="sidebox-title">推荐课程</h4>
        </div>
        <div class="sidebox-body course-content side-list-body" style="text-align:left">
          <a :href='"/courseDetail?id="+item.id' v-for="item in courseList"><img style="width:25px;height:25px"
                                                                                         :src="item.pic">
            {{item.title}}</a>
        </div>

      </div>


    </div>
  </div>
</template>

<script>
    import {send} from '../../static/js/comm'
    import fuwenben from '@/components/fuwenben'


    export default {
        name: "right",
        components: {
            fuwenben: fuwenben

        },
        data: function () {
            return {
                courseList: [],
                paths: [],
                reportList: [],
                disslist: [],
                title: '',
                types: 1,
                content: '',
                user_id: localStorage.getItem('user_id'),
                c: 0,
            }
        },
        methods: {
            showMesfromchild(data) {
                data['title'] = data['report_title'];
                data['content'] = data['report_content'];
                data['types'] = this.types
                data['user_id'] = localStorage.getItem('user_id');
                send('/api/dissubmit/', 'post', data).then((res) => {
                    if (res.data.code == 200) {
                        alert('发布成功')
                        $('#askquestion').modal('hide')

                    } else {
                        alert('发布失败')
                    }
                }).catch((error) => {
                    alert('网络错误，请稍后重试')
                })
            },
            shows: function () {
                if (localStorage.getItem('user_id') != undefined) {
                    $('#askquestion').modal('show');
                }
            },
        },
        mounted() {
            if (localStorage.getItem('user_id') != undefined) {
                send('/api/recommend/?user_id=' + localStorage.getItem('user_id'), 'get').then((res) => {
                    this.courseList = res.data.courseList
                })
            }
            ;
            send('/api/admin01/path/?limit=4', 'get').then((res) => {
                if (res.data.code == 200) {
                    this.paths = res.data.dataList
                }
            })

        }
    }
</script>

<style scoped>

</style>
