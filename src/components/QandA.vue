<template>
  <el-row class="role" style="display: flex; justify-content: flex-end">
    <el-card
      class="card"
      shadow="never"
      :body-style="{
        backgroundColor: 'rgba(0,0,0,.05)',
        borderRadius: '1vh',
        border: '0px solid ',
      }"
    >
      <div>{{ props.question }}</div>
    </el-card>
    <el-avatar :icon="UserFilled" size="large" style="margin-right: 1vw" />
  </el-row>
  <el-row class="role">
    <el-avatar size="large">Agent</el-avatar>
    <el-card
      class="card"
      shadow="never"
      :body-style="{
        backgroundColor: 'rgba(98,106,239,.1)',
        borderRadius: '1vh',
        border: '0px',
        maxWidth: '70vw',
      }"
    >
      <div>{{ props.answer.answer }}</div>
      <div style="margin-top: 3vh">
        The answer is generated according to the following papers.
      </div>
      <div
        v-for="info in props.answer.papers"
        v-bind:key="info"
        style="margin-top: 3vh"
      >
        <div>
          <div class="label">Title</div>
          <div class="paperInfo">{{ info.title }}</div>
        </div>
        <div>
          <div class="label">Author</div>
          <div v-if="info.author !== null" class="paperInfo">
            {{ info.author }}
          </div>
          <div v-else class="paperInfo">unknown</div>
        </div>
        <div>
          <div class="label">Source</div>
          <div v-if="info.detail !== 'unknown'" class="paperInfo">
            Visit <a ref="{{info.detail}}">{{ info.detail }}</a> to see
            details.<br />
            Visit <a ref="{{info.pdf}}">{{ info.pdf }}</a> to see the paper.
          </div>
          <div v-else class="paperInfo">
            404-Can't find the paper's source page
          </div>
        </div>
        <div>
          <div class="label">Categories</div>
          <div class="paperInfo">{{ info.categories }}</div>
        </div>
      </div>
    </el-card>
  </el-row>
</template>

<script lang="ts" setup>
import { UserFilled } from "@element-plus/icons-vue";
import { AIAnswer } from "@/utils/paperInfo";
const props = defineProps<{
  question: string;
  answer: AIAnswer;
}>();
</script>

<style scoped>
.role {
  margin-top: 2vh;
  margin-bottom: 2vh;
}
.card {
  margin-left: 0.5vw;
  margin-right: 0.5vw;
}
.label {
  font-family: "Bell MT";
  font-weight: 1000;
  color: #626aef;
  width: 10vw;
  display: inline-flex;
}
.paperInfo {
  display: inline-flex;
  max-width: 55vw;
  font-family: "Roboto Light", "Ubuntu Light", "Ubuntu", monospace;
}
/deep/.el-card {
  border: none;
}
</style>
