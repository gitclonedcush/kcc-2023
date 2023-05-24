using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class PositionRocketScript : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        var startDisc = GameObject.Find("Start");

        if (startDisc != null)
        {
            gameObject.transform.position = startDisc.transform.position + new Vector3(0, 1, 0);
        }
    }

	private void OnTriggerEnter(Collider other)
	{
		if (other.name == "End")
        {
            var nextLevelScript = other.GetComponent<NextLevelScript>();
            if (nextLevelScript != null)
            {
                SceneManager.LoadScene(nextLevelScript.NextLevel);
            }
        }
	}
}
