import React, { useEffect, useState } from 'react'
import './App.scss'
import { useAppSelector, useAppDispatch } from './app/hooks'
import {
  selectPosts,
  selectStatus,
  // fetchPostsAsync,
  PostType,
  fetchPostsAsync,
} from './features/posts/postsSlice'
import { selectUser, logoutUser } from './features/auth/authSlice'
import Post from './components/Post'
import Image from './components/Widgets/Image'
import Button from './components/Widgets/Button'
import Modal from './components/Widgets/Modal'
import Logo from './components/Logo'
import Login from './components/Login'

function App() {
  const [openModal, setModal] = useState<boolean>(false)
  const posts = useAppSelector(selectPosts)
  const postsStatus = useAppSelector(selectStatus)
  const currentUser = useAppSelector(selectUser)
  const dispatch = useAppDispatch()

  useEffect(() => {
    dispatch(fetchPostsAsync())
  }, [])

  const logout = () => {
    dispatch(logoutUser())
  }

  return (
    <div className='app'>
      <div className='app_header'>
        <Logo className='app_header-image' />

        <div className='flex'>
          {currentUser?.authToken ? (
            <Button onClick={logout}>Logout</Button>
          ) : (
            <>
              <Button onClick={() => setModal(true)}>Login</Button>
              <Button>Signup</Button>
            </>
          )}
        </div>
      </div>
      <Modal open={openModal} onClose={setModal} title={<Logo />}>
        <Login closeModal={setModal} />
      </Modal>
      {posts?.length > 0 &&
        posts.map((item: PostType, idx: number) => (
          <Post key={idx} item={item} />
        ))}
    </div>
  )
}

export default App
