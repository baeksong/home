<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css">
  <meta charset="UTF-8">
  <title>취업 정보 계정 만들기</title>
</head>
<body>

  <div class="container mt-3">
    <h2 class="text-center fw-bold">취업 정보 계정 만들기</h2>
    <hr>
    <div class="text-danger">* 필수 입력 항목</div>

    <form>
      <!-- 기본 정보 -->
      <div class="my-3 p-2 bg-secondary text-white fw-bold">기본 정보</div>
      <div class="row">
        <div class="col-sm-6">
          <div class="my-3 me-3">
            <label for="name">이름<span class="text-danger">*</span></label>
            <input type="text" id="name" name="name" class="form-control" required>
          </div>
          <!-- 다른 필수 기본 정보 필드를 추가하세요 -->
        </div>

        <div class="col-sm-6">
          <div class="my-3 me-3">
            <label for="mobile">모바일 폰<span class="text-danger">*</span></label>
            <input type="tel" id="mobile" name="mobile" class="form-control" placeholder="010-0000-0000" required>
          </div>
          <!-- 다른 필수 기본 정보 필드를 추가하세요 -->
        </div>
      </div>

      <!-- 학 력 -->
      <div class="my-3 p-2 mt-4 bg-secondary text-white fw-bold">학 력</div>
      <div class="row">
        <div class="col-sm-6">
          <div class="my-3 me-3">
            <label for="school_name">학교명<span class="text-danger">*</span></label>
            <input type="text" id="school_name" name="school_name" class="form-control" required>
          </div>
          <!-- 다른 학력 관련 필드를 추가하세요 -->
        </div>
      </div>

      <!-- 업무 경력 -->
      <div class="my-3 p-2 mt-4 bg-secondary text-white fw-bold">업무 경력</div>
      <div class="row">
        <div class="col-sm-6">
          <div class="my-3 me-3">
            <label for="workplace">근무업체명</label>
            <input type="text" id="workplace" name="workplace" class="form-control">
          </div>
          <!-- 다른 업무 경력 관련 필드를 추가하세요 -->
        </div>
      </div>

      <!-- 자기소개서 -->
      <div class="my-3 p-2 mt-4 bg-secondary text-white fw-bold">자기소개서</div>
      <div class="col-md-6">
        <label for="attachment">첨부 파일</label>
        <input type="file" class="form-control" id="attachment" name="attachment">
      </div>

      <div class="my-4 text-center">
        <input type="submit" class="btn btn-primary" value="제출">
        <input type="reset" class="btn btn-primary" value="재작성">
      </div>
    </form>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>