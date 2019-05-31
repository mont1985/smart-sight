<template>
  <footer class="footer px-4">
    <div class="row d-flex align-items-center justify-content-lg-around">
      <div class="col-lg-6">
        <div class="copyright text-center text-lg-left text-muted">
          © {{ year }}
          <a
            href="https://lewis-munyi.github.io"
            class="font-weight-bold ml-1"
            target="_blank"
            >Lewis Munyi</a
          >
        </div>
      </div>
      <div class="col-lg-6">
        <ul
          class="nav nav-footer justify-content-center justify-content-lg-end"
        >
          <li class="nav-item">
            <a href="https://uonbi.ac.ke" class="nav-link" target="_blank"
              >University of Nairobi</a
            >
          </li>
          <li class="nav-item">
            <a
              href="https://github.com/lewis-munyi/smart-sight/blob/master/deep-learning/LICENSE"
              class="nav-link"
              target="_blank"
              >MIT License</a
            >
          </li>
        </ul>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  data() {
    return {
      year: new Date().getFullYear()
    };
  }
};
</script>
<style></style>
